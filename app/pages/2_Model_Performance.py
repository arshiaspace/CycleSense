"""
Model Performance Dashboard
CycleSense
"""

from pathlib import Path
import sys

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# -------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

REPORT_DIR = PROJECT_ROOT / "reports"

# -------------------------------------------------------

st.set_page_config(
    page_title="Model Performance",
    page_icon="📊",
    layout="wide"
)

st.title("Model Performance")

st.write(
    """
This dashboard summarizes the performance of all machine learning
models evaluated during the CycleSense project.
"""
)

st.markdown("---")

# -------------------------------------------------------
# Load Results
# -------------------------------------------------------

try:

    regression = pd.read_csv(
        REPORT_DIR / "regression_results.csv"
    )

    classification = pd.read_csv(
        REPORT_DIR / "classification_results.csv"
    )

except Exception as e:

    st.error(e)

    st.stop()

# -------------------------------------------------------
# Best Models
# -------------------------------------------------------

best_reg = regression.loc[
    regression["R²"].idxmax()
]

best_cls = classification.loc[
    classification["Accuracy"].idxmax()
]

st.header("Best Models")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Best Regression Model",
        best_reg["Model"]
    )

    st.metric(
        "R² Score",
        f"{best_reg['R²']:.3f}"
    )

with col2:

    st.metric(
        "Best Classification Model",
        best_cls["Model"]
    )

    st.metric(
        "Accuracy",
        f"{best_cls['Accuracy']:.3f}"
    )

st.markdown("---")

# -------------------------------------------------------
# Regression Results
# -------------------------------------------------------

st.subheader("Regression Results")

st.dataframe(
    regression,
    use_container_width=True,
    hide_index=True
)

# -------------------------------------------------------
# Regression Chart
# -------------------------------------------------------

fig, ax = plt.subplots(figsize=(8,4))

ax.bar(
    regression["Model"],
    regression["R²"]
)

ax.set_ylabel("R² Score")

ax.set_title("Regression Model Comparison")

plt.xticks(rotation=15)

st.pyplot(fig)

# -------------------------------------------------------
# Classification Results
# -------------------------------------------------------

st.subheader("Classification Results")

st.dataframe(
    classification,
    use_container_width=True,
    hide_index=True
)

# -------------------------------------------------------
# Classification Chart
# -------------------------------------------------------

fig, ax = plt.subplots(figsize=(8,4))

ax.bar(
    classification["Model"],
    classification["Accuracy"]
)

ax.set_ylabel("Accuracy")

ax.set_title("Classification Model Comparison")

plt.xticks(rotation=15)

st.pyplot(fig)

# -------------------------------------------------------
# Winner Summary
# -------------------------------------------------------

st.markdown("---")

st.success(
f"""
### Best Regression Model

**{best_reg['Model']}**

• MAE : **{best_reg['MAE']:.2f}**

• RMSE : **{best_reg['RMSE']:.2f}**

• R² Score : **{best_reg['R²']:.3f}**
"""
)

st.success(
f"""
### Best Classification Model

**{best_cls['Model']}**

• Accuracy : **{best_cls['Accuracy']:.3f}**

• Precision : **{best_cls['Precision']:.3f}**

• Recall : **{best_cls['Recall']:.3f}**

• F1 Score : **{best_cls['F1']:.3f}**

• ROC-AUC : **{best_cls['ROC-AUC']:.3f}**
"""
)

# -------------------------------------------------------
# Conclusion
# -------------------------------------------------------

st.markdown("---")

st.info(
"""
### Conclusion

- **Gradient Boosting Regressor** achieved the highest performance for predicting the estimated day of ovulation.

- **Gradient Boosting Classifier** achieved the best overall classification performance.

These models were selected for deployment in the CycleSense application based on their superior predictive performance across the evaluation metrics.
"""
)

st.markdown("---")

st.caption(
    "CycleSense • Machine Learning Performance Dashboard"
)