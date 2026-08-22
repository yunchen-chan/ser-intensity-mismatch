# Data

Raw audio is not included in this repository. Download each corpus from its official source and comply with its license and citation requirements.

- **RAVDESS:** [Zenodo record](https://zenodo.org/records/1188976) — CC BY-NC-SA 4.0.
- **Berlin Database of Emotional Speech (EMO-DB):** [TU Berlin project page](https://www.tu.berlin/kw/forschung/projekte/emotionale-sprechweise).
- **CREMA-D:** [official GitHub repository](https://github.com/CheyneyComputerScience/CREMA-D) — see the repository for its ODbL licensing terms.

`ravdess_intensity_features.csv` contains 576 path-sanitized RAVDESS speech rows from 24 actors for Happy, Sad, and Angry at Normal and Strong intensity. It supplies the 31 acoustic features used by the public core intensity-mismatch notebook. It does not contain audio, filenames, storage paths, or volunteer data. Two source recordings have identical extracted feature vectors and are intentionally retained as separate observations. Two zero-valued pitch-extraction failures are identified and converted to missing values inside the notebook before fold-specific median imputation.

`ser_features_sample.csv` contains 20 path-sanitized rows from the extracted RAVDESS feature table. It is included only to document the processed-data schema. The original Google Drive paths were removed.

The external volunteer recordings are not published because they contain identifiable voices and were collected only for a small exploratory pilot.
