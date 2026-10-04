# JNU-CTG: A Large-Scale Continuous Cardiotocography Dataset for Fetal Well-being Assessment

> **Version 1.0.0**
>
> Jinan University Clinical CTG Dataset — 20,769 continuous 30-minute CTG recordings from 12,606 unique pregnancies.

---

## Dataset Summary

The JNU-CTG dataset is a large-scale, open-access cardiotocography (CTG) repository comprising **20,769 continuous 30-minute recordings** collected from **12,606 unique pregnancies** during routine antepartum monitoring at the First Affiliated Hospital of Jinan University (Guangzhou, China). Each recording contains synchronized **fetal heart rate (FHR)** and **uterine contraction (UC)** signals sampled at 4 Hz (7,200 samples per channel). The dataset is paired with extensive clinical metadata (215 columns) including maternal demographics, pregnancy complications, delivery parameters, neonatal biometrics, detailed Apgar scores with sub-scores at 1/5/10 minutes, neonatal asphyxia diagnoses, and 108 pre-extracted engineered features spanning time, frequency, time-frequency, and deep learning domains.

All 20,769 recordings are publicly released. The `patient_id` field enables patient-level data splitting to ensure statistical independence, with the independent subset containing 12,606 recordings (one per pregnancy).

---

## Background

Cardiotocography is the global gold standard for antepartum fetal monitoring. However, traditional visual interpretation of CTG traces exhibits substantial inter-observer variability. While deep learning-driven automated diagnostic systems offer a solution, their development is bottlenecked by an acute scarcity of large-scale, publicly accessible waveform datasets. The only widely-used open-access CTG database — CTU-UHB — contains only 552 patients. JNU-CTG bridges this gap with an unprecedented scale in the open-source obstetric domain.

---

## Data Description

### Waveform Files (`waveforms/csv_raw_7200/`)

Each CSV file represents a **30-minute CTG segment** (7,200 consecutive samples) extracted from a longer raw monitoring session, starting at 5 minutes to exclude the initial sensor stabilization period.

| Property | Value |
|---|---|
| Number of files | 20,769 |
| Sampling rate | 4 Hz |
| Duration | 30 minutes (7,200 samples) |
| Columns | `FHR`, `UC` |
| FHR unit | beats per minute (bpm) |
| UC unit | arbitrary units (a.u.) |
| File format | CSV (UTF-8, comma-separated) |
| Rows per file | 7,201 (1 header + 7,200 data) |
| Missing value encoding | **0** (zero) — raw, unprocessed |

**File naming convention:** `{patient_id}_{gravidity}_{timestamp}.csv`

The filename (without `.csv`) corresponds exactly to the `record_id` in `metadata.csv`.

**Important:** Missing or invalid signal segments are encoded as **zero (0)**, not NaN. FHR values of 0 bpm are physiologically implausible in a live fetus and should be replaced with NaN before interpolation or filtering. UC values of 0 may represent either true zero-amplitude readings or missing data.

### Metadata File (`metadata.csv`)

A UTF-8 encoded CSV file with **20,769 rows × 215 columns**, serving as the master clinical registry. Each row corresponds to one recording.

**Key Columns:**

| Column | Type | Description |
|---|---|---|
| `record_id` | str | Unique recording identifier (matches waveform filename, e.g. `10000_1_210208000001`) |
| `patient_id` | int | Deidentified patient identifier — **use for patient-level splitting** |
| `figo_label` | int | FIGO morphological label: 0 = Normal, 1 = Abnormal |
| `apgar_1min` | int | Apgar total score at 1 minute |
| `apgar_5min` | int | Apgar total score at 5 minutes |
| `apgar_10min` | int | Apgar total score at 10 minutes |
| `apgar_1min_color` | int | Apgar sub-score: skin color at 1 min |
| `apgar_1min_heart_rate` | int | Apgar sub-score: heart rate at 1 min |
| `apgar_1min_respiration` | int | Apgar sub-score: respiration at 1 min |
| `apgar_1min_reflex` | int | Apgar sub-score: reflex at 1 min |
| `apgar_1min_muscle_tone` | int | Apgar sub-score: muscle tone at 1 min |
| `apgar_5min_*` | int | Apgar sub-scores at 5 minutes (same 5 components) |
| `apgar_10min_*` | int | Apgar sub-scores at 10 minutes (same 5 components) |
| `neonatal_asphyxia` | int | Clinical diagnosis: 0 = No, 1 = Yes |
| `maternal_age` | float | Maternal age (years) |
| `bmi` | float | Body mass index (kg/m²) |
| `gestational_age` | str | Gestational age (e.g., "38", "39+5") |
| `gravidity` | int | Number of pregnancies |
| `parity` | int | Number of births |
| `birth_weight_kg` | float | Birth weight (kg) |
| `delivery_spontaneous_vaginal` | bool | Spontaneous vaginal delivery |
| `delivery_cesarean` | bool | Cesarean section |
| `pregnancy_anemia` | int | Pregnancy anemia (0/1) |
| `gestational_diabetes` | int | Gestational diabetes mellitus (0/1) |
| `gestational_hypertension` | int | Gestational hypertension (0/1) |
| `oligohydramnios` | int | Oligohydramnios (0/1) |
| `meconium_stained_amniotic_fluid` | int | MSAF (0/1) |
| `F_BL` through `NetFea_4` | float | 108 pre-extracted engineered features |
| *(…207 additional columns)* | | *(See data dictionary for full list)* |

**Metadata Domains (215 columns organized by category):**

| Domain | Columns | Description |
|---|---|---|
| Identifiers | 2 | `record_id`, `patient_id` |
| Maternal Demographics | 5 | Age, BMI, height, weight, gravidity, parity |
| Labor & Delivery | 18 | Labor duration (total + stages), delivery mode (6 binary flags) |
| Neonatal Biometrics | 7 | Birth weight, head circumference, length, sex (4 binary flags) |
| Apgar Scores & Sub-scores | 18 | Total scores + 5 sub-scores × 3 time points (1/5/10 min) |
| Amniotic Fluid | 6 | Clarity grade, blood, volume |
| Placenta & Membranes | 17 | Delivery mode, integrity, dimensions, weight, defects |
| Perineal Conditions | 10 | Episiotomy, tears, lacerations |
| Pregnancy Complications | 12 | Anemia, GDM, hypertension, FGR, oligohydramnios, PROM, MSAF, etc. |
| Fetal Ultrasound | 5 | BPD, AC, FL, HC, presentation |
| Engineered Features (FHR) | 55 | Time-domain, frequency-domain, STFT, CWT, S-transform features |
| Engineered Features (UC) | 23 | UC signal statistics and time-frequency features |
| Cross-Signal Features (FHR–UC) | 25 | Wavelet coherence and cross-wavelet features |
| Deep Latent Features | 5 | Neural network encoder representations (`NetFea_0`–`NetFea_4`) |
| Outcome Labels | 2 | `figo_label`, `neonatal_asphyxia` |
| Other | 5 | Additional clinical variables |

### Code (`code/`)

| File | Description |
|---|---|
| `example_usage.py` | Minimal working example: signal loading, visualization, patient-level CV splitting |

---

## Cohort Summary

| Property | Value |
|---|---|
| Total recordings | 20,769 |
| Independent pregnancies | 12,606 |
| Mean recordings per patient | 1.65 (range: 1–10) |
| Maternal age (mean ± SD) | 29.55 ± 4.27 years |
| Gestational age at delivery (mean) | 39.22 weeks |
| FIGO Normal | 9,598 (46.2%) |
| FIGO Abnormal | 11,171 (53.8%) |
| Neonatal asphyxia (recordings) | 154 (0.74%) |
| Neonatal asphyxia (unique patients) | 91 (0.72%) |
| Spontaneous vaginal delivery | 83.7% |
| Cesarean section | 16.3% |
| Signal dropout: FHR (mean) | 5.8% zero-valued samples |
| Signal dropout: UC (mean) | 0.8% zero-valued samples |

### Recordings per Patient Distribution

| Recordings | Patients | % |
|---|---|---|
| 1 | 7,483 | 59.4% |
| 2 | 3,140 | 24.9% |
| 3 | 1,272 | 10.1% |
| 4 | 474 | 3.8% |
| 5 | 162 | 1.3% |
| 6–10 | 75 | 0.6% |

---

## Directory Structure

```
JNU-CTG/
├── metadata.csv                              # Master metadata (20,769 rows × 215 columns)
├── README.md                                 # This file
├── code/
│   └── example_usage.py                      # Minimal working example (Python)
├── waveforms/
│   └── csv_raw_7200/                         # Raw waveform files (20,769 CSV files)
│       ├── 10000_1_210208000001.csv          # FHR + UC, 7,200 samples each
│       ├── 10003_1_210208000001.csv
│       └── ...                               # 20,767 remaining files
```

---

## Getting Started

### Requirements

- Python ≥ 3.8
- pandas, NumPy
- (Optional) matplotlib, scikit-learn for the full example

### Quick Start

```python
import pandas as pd
import numpy as np

# Load metadata
metadata = pd.read_csv('metadata.csv', encoding='utf-8-sig')
print(f"Loaded {len(metadata)} recordings from {metadata['patient_id'].nunique()} patients")

# Load a waveform file
waveform = pd.read_csv('waveforms/csv_raw_7200/10000_1_210208000001.csv')
fhr = waveform['FHR'].values.astype(np.float32)  # (7200,) — beats per minute
uc = waveform['UC'].values.astype(np.float32)    # (7200,) — relative units

# Handle missing values: replace 0 with NaN
fhr = np.where(fhr == 0, np.nan, fhr)
uc = np.where(uc == 0, np.nan, uc)

# Quick stats
print(f"FHR: mean={np.nanmean(fhr):.1f} bpm, missing={np.isnan(fhr).mean()*100:.1f}%")
print(f"UC:  mean={np.nanmean(uc):.1f}, missing={np.isnan(uc).mean()*100:.1f}%")
```

A complete working example with signal visualization and patient-level cross-validation is provided in [`code/example_usage.py`](code/example_usage.py).

---

## Important Usage Notes

1. **Missing values are encoded as 0 (zero)**, not NaN. Replace `FHR == 0` with NaN before interpolation or filtering. True FHR cannot be 0 bpm in a live fetus.

2. **Patient-level splitting is essential.** 59.4% of patients have only 1 recording, but the remainder have 2–10 recordings. Use `patient_id` with scikit-learn's `GroupKFold` (or equivalent) to prevent data leakage. For strict independence, restrict to the first recording per patient (yields 12,606 recordings).

3. **No umbilical arterial pH.** Unlike CTU-UHB and some other CTG databases, JNU-CTG does not include cord blood gas analysis. Use Apgar scores (with component-level sub-scores) and neonatal asphyxia diagnosis as outcome endpoints.

4. **Class imbalance in clinical outcomes.** Neonatal asphyxia occurs in only 0.72% of unique patients (n = 91). Use AUC-ROC and AUC-PR rather than accuracy. Prevalence-dependent metrics should not be interpreted as estimates of real-world clinical performance without appropriate adjustment.

5. **Raw signal quality.** The released waveforms are unprocessed — no interpolation, filtering, or imputation has been applied. FHR zero-rate averages ~5.9% across the cohort (median ~0.7%); UC zero-rate averages ~1.0% (median 0.0%). Apply your own quality filtering pipeline.

6. **Antepartum recordings.** All recordings were collected during routine antepartum monitoring (typically 1–2 weeks prior to delivery). The dataset does not contain intrapartum (during labor) recordings.

7. **Single-center cohort.** All data originate from a single tertiary medical center in Southern China. External validation on diverse populations is recommended for models intended for clinical deployment.

8. **Not a clinical tool.** JNU-CTG is provided for research and educational purposes only. It must not be used to guide patient care.

---

## Data Acquisition Details

**Monitoring equipment.** Continuous fetal monitoring was performed using commercial clinical fetal monitors (LM-F0, LM-F1B, LM-F3, and LM-F5 systems) at the First Affiliated Hospital of Jinan University. Fetal heart rate was recorded using external Doppler ultrasound probes; uterine contractions were recorded using external tocodynamometry sensors.

**Annotation.** All 20,769 CTG segments were manually classified as Normal or Abnormal following the FIGO diagnostic criteria by two senior obstetricians (Zheng Zheng and Xiuyu Pan) from Guangzhou Women and Children's Medical Center, each with over seven years of experience in CTG interpretation. Discrepant cases were resolved through consensus discussion.

**Outcome definitions.** Neonatal asphyxia was defined according to Chinese Medical Association Perinatal Medicine Branch guidelines: 1-minute or 5-minute Apgar score ≤ 7, accompanied by clinical signs of respiratory depression or need for positive pressure ventilation. Apgar scores include component-level sub-scores (color, heart rate, respiration, reflex, muscle tone) at 1, 5, and 10 minutes.

**Deidentification.** All personally identifiable information has been permanently removed. `patient_id` is an anonymized integer unrelated to original hospital record numbers. Absolute timestamps are removed; signals are indexed by sample number (0–7,199). Selected continuous variables were categorized or rounded to reduce re-identification risk.

---

## Ethics Statement

This study was approved by the Institutional Review Board of the First Affiliated Hospital of Jinan University (Approval No. JNUKY-2022-018). Given the retrospective utilization of fully deidentified historical records, the requirement for individual informed consent was formally waived. Authorization was obtained for the public release of the anonymized data.

---

## License

This dataset is distributed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

You are free to:
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material for any purpose, even commercially

Under the following terms:
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made.

---

## Citation

If you use the JNU-CTG dataset in your research, please cite:

> [Insert full citation: Authors. "A Large-Scale Continuous Cardiotocography Dataset for Fetal Hypoxia Prediction." *Journal Name*, Year. DOI: Insert DOI.]

---

## Contact

For questions or issues regarding the dataset, please contact:

- **Repository:** [Insert GitHub URL]
- **Email:** [Insert Contact Email]

---

## Version History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026 | Initial public release: 20,769 recordings, 215 metadata columns, 108 engineered features |

---

## References

1. Ayres-de-Campos D, Spong CY, Chandraharan E. FIGO consensus guidelines on intrapartum fetal monitoring: Cardiotocography. *Int J Gynecol Obstet*. 2015;131(1):13–24.
2. Chudáček V, Spilka J, Burša M, et al. Open access intrapartum CTG database. *BMC Pregnancy Childbirth*. 2014;14:16.
3. Ben M'Barek I, Jauvion G, Merrer J, et al. DeepCTG® 2.0: Development and validation of a deep learning model to detect neonatal acidemia from cardiotocography during labor. *Comput Biol Med*. 2025;184:109448.
4. Ben M'Barek I, Jauvion G, Manceau H, et al. APHP-CTG: An Open-Access Multicentre Intrapartum Cardiotocography Database for Neonatal Acidaemia Prediction. *Sci Data*. 2026.
