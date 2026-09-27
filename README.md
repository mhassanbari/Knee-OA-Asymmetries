# Impact of Daily Physical Fatigue on Inter-Limb Load Asymmetry in Unilateral Knee Osteoarthritis

This repository contains the analysis codebase, statistical modeling scripts, and figure generation routines for the research study evaluating biomechanical load asymmetry under physical fatigue in individuals with unilateral knee osteoarthritis (OA)[cite: 1].

## Repository Overview
- `data/`: Contains participant data metadata schema and processed metrics[cite: 1].
- `scripts/01_data_preprocessing.py`: Signal filtering (4th-order Butterworth low-pass filter at 25 Hz) and load asymmetry index calculation[cite: 1].
- `scripts/02_asymmetry_analysis.py`: Statistical testing including paired t-tests and task-specific ANOVA[cite: 1].
- `scripts/03_regression_modeling.py`: Multiple linear regression analysis predicting asymmetry changes from WOMAC, Age, and BMI[cite: 1].
- `scripts/04_generate_figures.py`: Codebase generating study visualizations[cite: 1].

## Environment Setup
Python version requirement: `3.9.7`[cite: 1]

Install required libraries:
```bash
pip install -r requirements.txt