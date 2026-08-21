# Model artifacts

`ser_fusion_svm_model.joblib` is the saved RAVDESS fusion-feature classification pipeline. It contains:

- `StandardScaler`
- `SVC` with the default RBF kernel and `class_weight="balanced"`

`feature_names.json` stores the ordered 31-feature input schema expected by the model.

The artifact was originally saved with scikit-learn 1.6.1, so the repository pins that version for compatibility. Joblib/pickle files can execute code when loaded; load this file only if you trust the repository source.

