"""
Data Loading Utilities
"""

import pandas as pd
from src.config import RAW_DATA_PATH

def load_data():
    try:
        df = pd.read_csv(RAW_DATA_PATH)
        print(f"Dataset loaded successfully.")
        print(f"Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print("Dataset not found.")
        print(RAW_DATA_PATH)
        raise