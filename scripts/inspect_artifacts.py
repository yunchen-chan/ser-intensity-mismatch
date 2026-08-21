"""Inspect the public sample table and saved model artifacts.

This script does not retrain the experiments. It provides a quick integrity check
for the small artifacts included in the repository.
"""

from __future__ import annotations

import json
from pathlib import Path

import joblib
import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_PATH = REPO_ROOT / "data" / "ser_features_sample.csv"
MODEL_PATH = REPO_ROOT / "models" / "ser_fusion_svm_model.joblib"
FEATURE_NAMES_PATH = REPO_ROOT / "models" / "feature_names.json"


def main() -> None:
    sample = pd.read_csv(SAMPLE_PATH)
    with FEATURE_NAMES_PATH.open("r", encoding="utf-8") as file:
        feature_names = json.load(file)
    model = joblib.load(MODEL_PATH)

    missing_features = [name for name in feature_names if name not in sample.columns]

    print(f"Sample shape: {sample.shape}")
    print(f"Expected model features: {len(feature_names)}")
    print(f"Missing expected features: {missing_features}")
    print(f"Model type: {type(model).__name__}")
    print(f"Pipeline steps: {list(model.named_steps)}")


if __name__ == "__main__":
    main()

