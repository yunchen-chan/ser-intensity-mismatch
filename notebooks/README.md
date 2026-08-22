# Notebooks

`SER_Intensity_Mismatch_Public.ipynb` is the core public experiment. It runs all six Normal, Strong, and Mixed train/test conditions from `data/ravdess_intensity_features.csv` using fixed speaker-independent actor folds. It displays the original archived report scores beside a clearly labeled fixed public rerun.

`SER_Three_Corpus_Baseline_Public.ipynb` contains the cleaned public workflow for the speaker-independent three-corpus baseline using RAVDESS, EMO-DB, and CREMA-D. Rerunning that extension requires obtaining the original corpora and configuring the local data paths described in the notebook.

For the core notebook, install the repository requirements and run the cells from top to bottom. The public RAVDESS intensity feature table is already included; raw audio is not required for this rerun.
