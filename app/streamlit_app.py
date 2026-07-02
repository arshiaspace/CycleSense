"""
CycleSense
Main Streamlit Application
"""

from pathlib import Path
import sys

import streamlit as st

# ---------------------------------------------------------
# Project Imports
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.utils import load_model
from src.config import MODEL_DIR
from app.prepare_input import prepare_input

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="CycleSense",
    page_icon="🌸",
    layout="wide"
)

# ---------------------------------------------------------
# Custom CSS
# ---------------------------------------------------------

st.markdown("""
<style>

section.main > div{
    padding-top:1rem;
}

.block-container{
    padding-top:1rem;
    padding-bottom:2rem;
}

.small-text{
    color:#808080;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Load Model
# ---------------------------------------------------------

try:

    model = load_model(
        MODEL_DIR / "best_ovulation_model.pkl"
    )

except Exception as e:

    st.error(f"Could not load model.\n\n{e}")
    st.stop()

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

st.sidebar.title("🌸 CycleSense")

st.sidebar.info(
"""
CycleSense predicts the **Estimated Day of Ovulation**
using a Gradient Boosting Regression model trained on the
Federal Menstrual Cycle Dataset.

Use the navigation menu above to explore:

• Home

• About

• Model Performance

• SHAP Insights
"""
)

# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title("🌸 CycleSense")

st.subheader(
    "Research-Based Ovulation Prediction using Machine Learning"
)

st.write(
"""
CycleSense is an AI-powered application that predicts the
**Estimated Day of Ovulation** using menstrual cycle
characteristics.

The prediction model was trained on the Federal Menstrual
Cycle Dataset and achieved the best performance using a
**Gradient Boosting Regressor**.
"""
)

st.divider()

# ---------------------------------------------------------
# Input Form
# ---------------------------------------------------------

st.header("Enter Cycle Information")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=15,
        max_value=55,
        value=28
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=50.0,
        value=22.5
    )

    cycle_length = st.number_input(
        "Length of Cycle",
        min_value=20,
        max_value=45,
        value=28
    )

    mean_cycle = st.number_input(
        "Mean Cycle Length",
        min_value=20.0,
        max_value=45.0,
        value=28.0
    )

with col2:

    menses_length = st.number_input(
        "Length of Menses",
        min_value=2,
        max_value=10,
        value=5
    )

    mean_menses = st.number_input(
        "Mean Menses Length",
        min_value=2.0,
        max_value=10.0,
        value=5.0
    )

    intercourse_days = st.number_input(
        "Number of Days of Intercourse",
        min_value=0,
        max_value=30,
        value=2
    )

    fertile_window = st.selectbox(
        "Intercourse in Fertile Window",
        options=[0, 1],
        format_func=lambda x: "Yes" if x else "No"
    )

predict_button = st.button(
    "🔮 Predict Ovulation Day",
    use_container_width=True
)

# ---------------------------------------------------------
# Prediction
# ---------------------------------------------------------

if predict_button:

    user_inputs = {
        "Age": age,
        "BMI": bmi,
        "LengthofCycle": cycle_length,
        "MeanCycleLength": mean_cycle,
        "LengthofMenses": menses_length,
        "MeanMensesLength": mean_menses,
        "NumberofDaysofIntercourse": intercourse_days,
        "IntercourseInFertileWindow": fertile_window
    }

    X_input = prepare_input(user_inputs)

    try:

        prediction = model.predict(X_input)[0]
        prediction = int(round(float(prediction)))

        st.divider()

        st.subheader("🌸 Prediction Result")

        result_col1, result_col2 = st.columns([2, 1])

        with result_col1:

            st.success(
                f"""
### Estimated Ovulation Day

**Day {prediction}**
"""
            )

            st.info(
                """
The prediction is generated using the best-performing
Gradient Boosting Regression model trained on the
Federal Menstrual Cycle Dataset.
"""
            )

        with result_col2:

            st.metric(
                label="Predicted Day",
                value=f"Day {prediction}"
            )

    except Exception as e:

        st.error(f"Prediction failed.\n\n{e}")

# ---------------------------------------------------------
# Project Summary
# ---------------------------------------------------------

st.divider()

st.header("📊 Project Summary")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        label="Best Model",
        value="Gradient Boosting"
    )

with col2:

    st.metric(
        label="Prediction Type",
        value="Regression"
    )

with col3:

    st.metric(
        label="Dataset",
        value="1665 Cycles"
    )

# ---------------------------------------------------------
# About the Model
# ---------------------------------------------------------

st.divider()

st.subheader("🧠 About the Prediction")

st.write(
"""
This application predicts the **Estimated Day of Ovulation**
using a machine learning model trained on menstrual cycle
characteristics.

The model was selected after comparing multiple regression
algorithms, including:

- Linear Regression
- Ridge Regression
- Random Forest Regression
- Gradient Boosting Regression

Gradient Boosting achieved the best overall performance and
was selected as the final deployed model.
"""
)

# ---------------------------------------------------------
# Disclaimer
# ---------------------------------------------------------

st.divider()

st.warning(
"""
### Disclaimer

CycleSense is intended for **educational and research purposes only**.

It is **not a medical device** and should not be used for
medical diagnosis, treatment, contraception, or fertility
planning.

Please consult a qualified healthcare professional for
medical advice.
"""
)

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.divider()

st.caption(
    "Developed as part of the CycleSense Machine Learning Project • Women's Health AI"
)