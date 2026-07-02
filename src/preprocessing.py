"""
Data Preprocessing Module

This module contains reusable functions for cleaning the
Federal Menstrual Cycle Dataset.
"""

import numpy as np
import pandas as pd


def replace_blank_with_nan(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replace blank strings and whitespace with NaN.
    """
    df = df.copy()

    df.replace(r'^\s*$', np.nan, regex=True, inplace=True)

    return df


def drop_identifier_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove identifier columns.
    """
    df = df.copy()

    identifier_columns = [
        "ClientID"
    ]

    existing_columns = [
        col for col in identifier_columns
        if col in df.columns
    ]

    df.drop(columns=existing_columns, inplace=True)

    return df


def convert_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert object columns to numeric wherever possible.
    """
    df = df.copy()

    for column in df.columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="ignore"
        )

    return df


def remove_missing_targets(
    df: pd.DataFrame,
    target: str = "EstimatedDayofOvulation"
) -> pd.DataFrame:
    """
    Remove rows with missing target values.
    """
    df = df.copy()

    if target in df.columns:
        df = df.dropna(subset=[target])

    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows.
    """
    df = df.copy()

    df = df.drop_duplicates()

    return df


def remove_leakage_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove features that leak future information about ovulation.

    These variables are only known after the cycle is complete and
    should not be used for prediction.
    """

    df = df.copy()

    leakage_columns = [

        "FirstDayofHigh",

        "TotalNumberofHighDays",

        "TotalHighPostPeak",

        "TotalNumberofPeakDays",

        "TotalDaysofFertility",

        "TotalFertilityFormula"

    ]

    existing_columns = [
        col for col in leakage_columns
        if col in df.columns
    ]

    df.drop(
        columns=existing_columns,
        inplace=True
    )

    return df


def preprocess_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Complete preprocessing pipeline.

    Steps:
    1. Replace blank values with NaN
    2. Remove identifier columns
    3. Convert numeric columns
    4. Remove rows with missing target
    5. Remove duplicate rows
    6. Remove data leakage features
    """

    df = replace_blank_with_nan(df)

    df = drop_identifier_columns(df)

    df = convert_numeric_columns(df)

    df = remove_missing_targets(df)

    df = remove_duplicates(df)

    df = remove_leakage_features(df)

    return df