# Implementation

## Project Workflow

The implementation follows a modular machine learning pipeline consisting of data preprocessing, feature engineering, model development, evaluation, explainability, and deployment.

---

# Project Structure

```
CycleSense/

├── app/
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── notebooks/
├── reports/
├── src/
└── README.md
```

---

# Step 1: Data Collection

The Federal Menstrual Cycle Dataset is stored under

```
data/raw/
```

The dataset contains menstrual cycle records together with demographic, reproductive, and physiological information.

---

# Step 2: Data Cleaning

The preprocessing stage includes:

- Removing duplicate records
- Replacing blank strings with missing values
- Converting numeric columns
- Handling missing values
- Removing identifier columns
- Removing leakage variables
- Standardizing feature types

The cleaned dataset is stored under:

```
data/processed/
```

---

# Step 3: Exploratory Data Analysis

EDA includes:

- Distribution analysis
- Missing value visualization
- Correlation analysis
- Target variable inspection
- Outlier detection

Visualizations are generated using Matplotlib and Seaborn.

---

# Step 4: Feature Engineering

Important preprocessing steps include:

- Median imputation
- Feature scaling
- Feature selection using SelectKBest
- Removal of highly correlated variables

Feature selection reduces dimensionality while improving model performance.

---

# Step 5: Model Development

Regression models evaluated:

- Linear Regression
- Ridge Regression
- Random Forest Regressor
- Gradient Boosting Regressor

Classification models evaluated:

- Logistic Regression
- Random Forest Classifier
- Gradient Boosting Classifier

Hyperparameter tuning is performed using GridSearchCV.

---

# Step 6: Model Evaluation

Regression metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

Classification metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

Performance reports are exported to the reports directory.

---

# Step 7: Explainability

SHAP is used to compute feature importance.

Outputs include:

- SHAP Summary Plot
- SHAP Feature Importance Rankings

These improve transparency of model predictions.

---

# Step 8: Deployment

The final Gradient Boosting model is serialized using Joblib.

The Streamlit application provides:

- User-friendly interface
- Ovulation prediction
- Model information
- Performance metrics
- SHAP feature importance

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- SHAP
- Matplotlib
- Seaborn
- Joblib
- Streamlit

---

# Final Outcome

The implementation results in an end-to-end machine learning application capable of predicting the estimated day of ovulation while providing interpretable insights into feature importance through SHAP explainability.