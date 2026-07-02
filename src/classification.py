"""
Classification Model Training
"""

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier


def build_classifier():

    pipeline = Pipeline([

        ("imputer", SimpleImputer(strategy="median")),

        ("model", RandomForestClassifier(
            random_state=42
        ))

    ])

    return pipeline