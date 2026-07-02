"""
Feature Engineering
"""

import pandas as pd


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create engineered features.
    """

    df = df.copy()

    if "Height" in df.columns and "Weight" in df.columns:

        df["Weight_per_Height"] = (
            df["Weight"] /
            df["Height"]
        )

    if "LengthofCycle" in df.columns and "LengthofMenses" in df.columns:

        df["MensesRatio"] = (
            df["LengthofMenses"] /
            df["LengthofCycle"]
        )

    return df