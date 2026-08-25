# Model artifacts

`ser_fusion_svm_model.joblib` is a saved four-class RAVDESS classification artifact for Angry, Happy, Neutral, and Sad. It contains:

- `StandardScaler`
- `SVC` with an RBF kernel and `class_weight="balanced"`

`feature_names.json` stores the ordered 31-feature input schema expected by the model.

This saved artifact is intended for model inspection and inference on compatible numeric feature rows. It is not the set of models used to reproduce the six reported intensity-mismatch conditions.

The public intensity notebook retrains a separate `SimpleImputer -> StandardScaler -> SVC` pipeline within each speaker-independent fold and does not load this `.joblib` file. The exact original training-row split used to save this artifact was not separately archived, so the artifact should not be treated as independent evidence of the reported six-condition scores.

The artifact was originally saved with scikit-learn 1.6.1, so the repository pins that version for compatibility. Joblib/pickle files can execute code when loaded; load this file only if you trust the repository source.
