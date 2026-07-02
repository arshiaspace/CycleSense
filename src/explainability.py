"""
SHAP Explainability Utilities
"""

import shap


def build_explainer(model):

    return shap.TreeExplainer(model)


def compute_shap_values(explainer, X):

    return explainer.shap_values(X)