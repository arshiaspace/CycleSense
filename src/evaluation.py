"""
Evaluation Utilities
"""

import numpy as np

from sklearn.metrics import (

    mean_absolute_error,

    mean_squared_error,

    r2_score,

    accuracy_score,

    f1_score

)


def regression_metrics(y_true, y_pred):

    return {

        "MAE": mean_absolute_error(y_true, y_pred),

        "RMSE": np.sqrt(
            mean_squared_error(y_true, y_pred)
        ),

        "R2": r2_score(y_true, y_pred)

    }


def classification_metrics(y_true, y_pred):

    return {

        "Accuracy": accuracy_score(
            y_true,
            y_pred
        ),

        "F1": f1_score(
            y_true,
            y_pred
        )

    }