# Machine-Learning-Based-Fetal-Well-being-Classification-Using-Cardiotocography-Features
Machine learning-based fetal well-being classification using 103 engineered CTG features from the JNU-CTG dataset. The project compares seven supervised ML models with patient-level data splitting, feature selection, hyperparameter tuning, and comprehensive evaluation.

## Project Structure
```
├── config/
│   └── config.py                    # Paths, random seed, split settings, model list
├── data/
│   ├── raw/                         # Original JNU-CTG dataset (not committed)
│   ├── processed/                   # Cleaned / split data
│   └── README.md
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_feature_selection.ipynb
│   ├── 04_model_training.ipynb
│   ├── 05_hyperparameter_tuning.ipynb
│   └── 06_model_evaluation.ipynb
├── results/
│   ├── figures/
│   ├── metrics/
│   └── feature_importance/
├── src/
│   ├── data_loader.py
│   ├── data_preprocessing.py
│   ├── feature_selection.py
│   ├── model_training.py
│   ├── hyperparameter_tuning.py
│   ├── model_evaluation.py
│   ├── visualization.py
│   └── utils.py
├── tests/
├── requirements.txt
└── README.md
```
