# Data

## Dataset
**JNU-CTG** — cardiotocography recordings with 103 engineered CTG features per sample, used for fetal well-being classification.

## Folder structure
| Folder | Contents |
|---|---|
| `raw/` | Original, unmodified dataset files. Never edit these. |
| `processed/` | Cleaned, split and scaled data produced by `02_data_preprocessing.ipynb` / `src/data_preprocessing.py`. |

## Notes
- Data files are not committed to Git (see `.gitignore`). Place the raw dataset in `data/raw/` before running the notebooks.
- Splitting is done at the **patient level** so recordings from the same patient never appear in both train and test sets.
