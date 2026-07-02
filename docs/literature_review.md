# Literature Review

## Introduction

Predicting the menstrual cycle and ovulation window has become an important application of machine learning in women's healthcare. Accurate ovulation prediction assists in fertility planning, reproductive health monitoring, and early identification of irregular menstrual patterns. Traditional calendar-based approaches often fail to account for the natural variability present in menstrual cycles, motivating the development of data-driven predictive models.

This project utilizes the Federal Menstrual Cycle Dataset to develop machine learning models capable of predicting the estimated day of ovulation while providing interpretable insights into the factors influencing the prediction.

---

# Existing Research

Several studies have investigated menstrual cycle prediction using statistical and machine learning approaches.

### Statistical Methods

Traditional prediction methods include:

- Calendar Method
- Rhythm Method
- Basal Body Temperature (BBT)
- Cervical Mucus Observation

Although widely used, these approaches assume relatively regular menstrual cycles and often perform poorly for individuals with variable cycle lengths.

---

### Machine Learning Approaches

Recent research has explored supervised learning algorithms including:

- Linear Regression
- Random Forest
- Gradient Boosting
- Support Vector Machines
- Neural Networks

These approaches incorporate multiple physiological and demographic variables to improve prediction accuracy over rule-based methods.

Gradient Boosting models have demonstrated strong performance due to their ability to capture nonlinear relationships among menstrual health variables.

---

# Explainable Artificial Intelligence

Healthcare applications require models that are interpretable rather than purely accurate.

Explainable AI techniques such as SHAP (SHapley Additive exPlanations) provide feature-level explanations by quantifying the contribution of each feature toward individual predictions.

The integration of SHAP improves model transparency and supports trustworthy AI in healthcare.

---

# Research Gap

Many existing studies focus primarily on predictive performance while providing limited interpretability.

Several publicly available implementations also lack:

- Modular project architecture
- Interactive user interfaces
- Explainability tools
- Reproducible preprocessing pipelines

This project addresses these limitations by combining machine learning, explainable AI, and an interactive Streamlit application.

---

# Proposed Solution

CycleSense proposes a complete end-to-end machine learning pipeline that includes:

- Data preprocessing
- Feature engineering
- Exploratory data analysis
- Regression modeling
- Classification modeling
- Feature selection
- SHAP explainability
- Interactive Streamlit deployment

The final model predicts the Estimated Day of Ovulation using Gradient Boosting Regression while providing interpretable feature importance rankings.

---

# Conclusion

Machine learning offers significant improvements over traditional ovulation estimation techniques by leveraging historical cycle characteristics and demographic information. By combining predictive performance with explainability, CycleSense demonstrates a practical framework for AI-assisted menstrual health analysis.