"""
SHAP Explainability Dashboard
CycleSense
"""

from pathlib import Path
import sys

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# -----------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

REPORT_DIR = PROJECT_ROOT / "reports"

# -----------------------------------------------------

st.set_page_config(
    page_title="SHAP Insights",
    page_icon="🔬",
    layout="wide"
)

st.title("Model Explainability")

st.write(
"""
Machine learning models often behave like black boxes.

To improve transparency, CycleSense uses **SHAP (SHapley Additive exPlanations)**,
which explains how each feature contributes to model predictions.

This helps users and researchers understand **why** a prediction was made.
"""
)

st.markdown("---")

# -----------------------------------------------------
# Load SHAP Importance
# -----------------------------------------------------

try:

    shap_df = pd.read_csv(
        REPORT_DIR / "shap_feature_importance.csv"
    )

except Exception as e:

    st.error(e)

    st.stop()

# -----------------------------------------------------
# Top Features Table
# -----------------------------------------------------

st.header("Top 10 Most Important Features")

st.dataframe(
    shap_df.head(10),
    use_container_width=True,
    hide_index=True
)

# -----------------------------------------------------
# Feature Importance Plot
# -----------------------------------------------------

st.markdown("---")

st.header("Feature Importance")

fig, ax = plt.subplots(figsize=(10,6))

ax.barh(
    shap_df.head(10)["Feature"][::-1],
    shap_df.head(10)["Importance"][::-1]
)

ax.set_xlabel("Mean Absolute SHAP Value")

ax.set_ylabel("Feature")

ax.set_title("Top 10 SHAP Feature Importances")

st.pyplot(fig)

# -----------------------------------------------------
# Interpretation
# -----------------------------------------------------

st.markdown("---")

st.header("Interpretation")

top5 = shap_df.head(5)

for _, row in top5.iterrows():

    st.success(
        f"**{row['Feature']}** was one of the strongest predictors used by the model."
    )

# -----------------------------------------------------
# Explain SHAP
# -----------------------------------------------------

st.markdown("---")

st.header("What is SHAP?")

st.write(
"""
SHAP is an explainable AI framework based on cooperative game theory.

Instead of only predicting an ovulation day, SHAP identifies **which features**
contributed most to the prediction and quantifies their influence.

Benefits include:

- Increased transparency
- Better trust in machine learning predictions
- Easier debugging of models
- More suitable for healthcare applications
"""
)

# -----------------------------------------------------
# Why Explainability Matters
# -----------------------------------------------------

st.markdown("---")

st.header("Why Explainability Matters in Healthcare")

st.info(
"""
Healthcare decisions require models that are not only accurate
but also interpretable.

Explainable AI helps clinicians and researchers understand
whether model predictions are based on medically meaningful
patterns rather than spurious correlations.

For this reason, SHAP has become one of the most widely used
methods for interpreting complex machine learning models.
"""
)

# -----------------------------------------------------
# Summary Metrics
# -----------------------------------------------------

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Features Analysed",
        len(shap_df)
    )

with col2:

    st.metric(
        "Top Features Displayed",
        10
    )

# -----------------------------------------------------
# Feature Ranking
# -----------------------------------------------------

st.markdown("---")

st.header("Complete Feature Ranking")

st.dataframe(
    shap_df,
    use_container_width=True,
    hide_index=True
)

# -----------------------------------------------------
# Footer
# -----------------------------------------------------

st.markdown("---")

st.caption(
    "CycleSense • Explainable Artificial Intelligence using SHAP"
)