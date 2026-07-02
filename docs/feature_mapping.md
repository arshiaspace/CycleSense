# Feature Mapping

## Objective

This document describes the role of each feature used throughout the CycleSense machine learning pipeline.

---

# Target Variables

| Feature | Type | Task |
|----------|------|------|
| EstimatedDayofOvulation | Numerical | Regression |
| LengthofCycle | Numerical | Regression |
| CycleWithPeakorNot | Binary | Classification |

---

# User Input Features (Streamlit)

The deployed application collects the following inputs from the user.

| Feature | Description |
|----------|-------------|
| Age | Age of participant |
| BMI | Body Mass Index |
| LengthofCycle | Current menstrual cycle length |
| MeanCycleLength | Average cycle length |
| LengthofMenses | Number of menstruation days |
| MeanMensesLength | Average menstruation length |
| NumberofDaysofIntercourse | Number of intercourse days |
| IntercourseInFertileWindow | Whether intercourse occurred during fertile window |

These values replace default feature values before prediction.

---

# Demographic Features

Examples include:

- Age
- BMI
- Height
- Weight
- Religion
- Ethnicity
- Schoolyears
- Marital Status

These describe participant characteristics.

---

# Reproductive Features

Examples include:

- Numberpreg
- Livingkids
- Miscarriages
- Abortions
- Breastfeeding
- ReproductiveCategory

These capture reproductive history.

---

# Menstrual Features

Examples include:

- LengthofCycle
- MeanCycleLength
- LengthofMenses
- MeanMensesLength
- TotalMensesScore
- MeanBleedingIntensity

These describe menstrual cycle characteristics.

---

# Behavioral Features

Examples include:

- NumberofDaysofIntercourse
- IntercourseInFertileWindow

These provide fertility-related behavioral information.

---

# Leakage Features

The following variables were excluded during preprocessing because they directly reveal information about ovulation.

- FirstDayofHigh
- TotalNumberofHighDays
- TotalHighPostPeak
- TotalNumberofPeakDays
- TotalDaysofFertility
- TotalFertilityFormula

Removing these features prevents target leakage and improves model generalization.

---

# Feature Selection

SelectKBest with Mutual Information was used during model development.

The feature selector retained the most informative variables for prediction while reducing dimensionality.

---

# Final Prediction Pipeline

User Input

↓

Prepare Complete Feature Vector

↓

Median Imputation

↓

Feature Selection

↓

Gradient Boosting Regression

↓

Estimated Day of Ovulation

---

# Summary

The final deployed model combines demographic, reproductive, menstrual, and behavioral information to predict the estimated day of ovulation. Careful preprocessing, leakage removal, and feature selection ensure that the model remains both accurate and interpretable.