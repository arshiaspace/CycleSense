# 🌸 CycleSense

> **An Explainable Machine Learning System for Ovulation Prediction using Menstrual Cycle Data**

CycleSense is an end-to-end machine learning application that predicts the **Estimated Day of Ovulation** from menstrual cycle characteristics using the **Federal Menstrual Cycle Dataset**. The project combines data preprocessing, feature engineering, predictive modeling, explainable AI (SHAP), and an interactive Streamlit dashboard.

---

## Features

- Comprehensive exploratory data analysis (EDA)
- Robust data cleaning and preprocessing pipeline
- Feature engineering and feature selection
- Multiple regression and classification models
- Hyperparameter tuning using GridSearchCV
- Best-performing Gradient Boosting Regression model
- SHAP-based explainable AI for model interpretability
- Interactive Streamlit web application
- Model performance dashboards
- Modular and production-ready project structure

---

## Dataset

**Dataset:** Federal Menstrual Cycle Dataset

The dataset contains menstrual cycle records together with demographic, reproductive, physiological, and behavioral information.

### Dataset Overview

| Attribute | Value |
|-----------|------:|
| Total Records | 1,653 |
| Original Features | 80 |
| Target Variable | EstimatedDayofOvulation |
| Problem Type | Regression + Classification |

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Explainability | SHAP |
| Deployment | Streamlit |
| Model Serialization | Joblib |

---

## Project Structure

```text
CycleSense/
│
├── app/
│   ├── pages/
│   ├── prepare_input.py
│   └── streamlit_app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   ├── feature_mapping.md
│   ├── implementation.md
│   └── literature_review.md
│
├── models/
│
├── notebooks/
│   ├── 01_data_overview.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_feature_understanding.ipynb
│   ├── 04_eda.ipynb
│   ├── 05_regression_modeling.ipynb
│   ├── 06_classification_modeling.ipynb
│   ├── 07_model_comparison.ipynb
│   └── 08_shap_explainability.ipynb
│
├── reports/
│
├── src/
│
├── README.md
├── requirements.txt
```

---

## Machine Learning Pipeline

```text
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Selection
      │
      ▼
Model Training
      │
      ▼
Hyperparameter Tuning
      │
      ▼
Model Evaluation
      │
      ▼
SHAP Explainability
      │
      ▼
Streamlit Deployment
```

---

## Models Evaluated

### Regression

- Linear Regression
- Ridge Regression
- Random Forest Regressor
- Gradient Boosting Regressor (Best)

### Classification

- Logistic Regression
- Random Forest Classifier
- Gradient Boosting Classifier

---

## Evaluation Metrics

### Regression

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

### Classification

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

---

## Explainable AI

CycleSense integrates **SHAP (SHapley Additive Explanations)** to improve model transparency.

SHAP enables:

- Global feature importance
- Local prediction explanations
- Feature contribution visualization
- Trustworthy AI predictions

---

## Streamlit Application

The application allows users to:

- Enter menstrual cycle information
- Predict the estimated day of ovulation
- Explore model performance
- View SHAP feature importance
- Learn about the project methodology

---

## Installation

Clone the repository.

```bash
git clone https://github.com/<your-username>/CycleSense.git

cd CycleSense
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the Streamlit application.

```bash
streamlit run app/streamlit_app.py
```

---

## Results

The **Gradient Boosting Regression** model achieved the best overall predictive performance among all evaluated regression models and was selected for deployment.

The project also demonstrates that explainable AI techniques such as SHAP can provide meaningful insight into the factors influencing ovulation prediction.

---


## Documentation

Additional documentation is available in the **docs/** directory.

- Literature Review
- Implementation Details
- Feature Mapping

---

## Future Improvements

- Collect real-world longitudinal cycle data
- Deep learning models (LSTM/Transformer)
- Confidence intervals for predictions
- Personalized fertility recommendations
- Cloud deployment
- Mobile application integration

---

## Disclaimer

CycleSense is intended solely for **educational and research purposes**.

It is **not a medical device** and should not be used for diagnosis, contraception, fertility planning, or medical decision-making. Always consult a qualified healthcare professional for medical advice.

---

## Author

**Arshia Anand**

Computer Engineering Student

Machine Learning • Data Science • AI • Full-Stack Development

GitHub: https://github.com/arshiaspace

LinkedIn: https://www.linkedin.com/in/arshia-anand-4649b32b2/

---

## Acknowledgements

- Federal Menstrual Cycle Dataset
- Scikit-learn
- SHAP
- Streamlit
- Open-source Python community

---

