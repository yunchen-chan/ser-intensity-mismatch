"""Inspect the public tables and saved model artifacts.

This script does not retrain the experiments. It provides a quick integrity check
for the artifacts included in the repository.
"""

from __future__ import annotations

import json
from pathlib import Path

import joblib
import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_PATH = REPO_ROOT / "data" / "ser_features_sample.csv"
INTENSITY_PATH = REPO_ROOT / "data" / "ravdess_intensity_features.csv"
INTENSITY_SUMMARY_PATH = REPO_ROOT / "results" / "intensity_summary.csv"
MODEL_PATH = REPO_ROOT / "models" / "ser_fusion_svm_model.joblib"
FEATURE_NAMES_PATH = REPO_ROOT / "models" / "feature_names.json"


def main() -> None:
    sample = pd.read_csv(SAMPLE_PATH)
    intensity = pd.read_csv(INTENSITY_PATH)
    intensity_summary = pd.read_csv(INTENSITY_SUMMARY_PATH)
    with FEATURE_NAMES_PATH.open("r", encoding="utf-8") as file:
        feature_names = json.load(file)
    model = joblib.load(MODEL_PATH)

    missing_features = [name for name in feature_names if name not in sample.columns]
    intensity_missing = [name for name in feature_names if name not in intensity.columns]
    model_features = list(getattr(model, "feature_names_in_", []))

    assert len(feature_names) == 31
    assert not missing_features
    assert not intensity_missing
    assert model_features == feature_names
    assert list(model.named_steps) == ["scaler", "classifier"]
    assert intensity.shape == (576, 34)
    assert intensity["actor_id"].nunique() == 24
    assert set(intensity["emotion"]) == {"Happy", "Sad", "Angry"}
    assert set(intensity["intensity"]) == {"Normal", "Strong"}
    assert len(intensity_summary) == 6

    print(f"Sample shape: {sample.shape}")
    print(f"Public intensity table shape: {intensity.shape}")
    print(f"Public intensity actors: {intensity['actor_id'].nunique()}")
    print(f"Expected model features: {len(feature_names)}")
    print(f"Missing expected features: {missing_features}")
    print(f"Model type: {type(model).__name__}")
    print(f"Pipeline steps: {list(model.named_steps)}")
    print(f"Identical feature rows retained: {intensity.duplicated().sum()}")
    print(f"Zero-valued pitch rows handled in notebook: {(intensity['pitch_mean'] == 0).sum()}")
    print(f"Archived intensity conditions: {len(intensity_summary)}")
    print("Artifact integrity checks passed.")


if __name__ == "__main__":
    main()
