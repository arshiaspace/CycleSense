"""
Prepare user input for prediction.

This module converts the few values entered by the user into
the complete feature vector expected by the trained model.
"""

import pandas as pd

from src.config import PROCESSED_DATA_DIR


# ---------------------------------------------------------
# Load Training Features
# ---------------------------------------------------------

X = pd.read_csv(
    PROCESSED_DATA_DIR / "X_ovulation.csv"
)

# ---------------------------------------------------------
# Compute Default Values
# ---------------------------------------------------------

# Median values for all numeric features
DEFAULT_VALUES = X.median(
    numeric_only=True
).to_dict()

# For any non-numeric columns (if present),
# use the most frequent value.

for column in X.columns:

    if column not in DEFAULT_VALUES:

        mode = X[column].mode()

        if len(mode):

            DEFAULT_VALUES[column] = mode.iloc[0]

        else:

            DEFAULT_VALUES[column] = 0


# ---------------------------------------------------------
# Prepare Input
# ---------------------------------------------------------

def prepare_input(user_inputs: dict) -> pd.DataFrame:
    """
    Build a complete feature vector for prediction.

    Parameters
    ----------
    user_inputs : dict
        Dictionary containing values entered in the Streamlit app.

    Returns
    -------
    pd.DataFrame
        Single-row dataframe with all required model features.
    """

    sample = DEFAULT_VALUES.copy()

    # Replace defaults with user values
    sample.update(user_inputs)

    # Ensure correct column order
    sample_df = pd.DataFrame([sample])

    sample_df = sample_df[X.columns]

    return sample_df


# ---------------------------------------------------------
# Optional Test
# ---------------------------------------------------------

if __name__ == "__main__":

    example = {

        "Age": 28,

        "BMI": 22.5,

        "LengthofCycle": 28,

        "MeanCycleLength": 28,

        "LengthofMenses": 5,

        "MeanMensesLength": 5,

        "NumberofDaysofIntercourse": 2,

        "IntercourseInFertileWindow": 1

    }

    prepared = prepare_input(example)

    print(prepared.head())

    print(prepared.shape)