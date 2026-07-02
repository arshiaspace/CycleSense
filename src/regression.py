"""
Regression Model Training
"""

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_regression
from sklearn.ensemble import GradientBoostingRegressor

from sklearn.model_selection import GridSearchCV


def build_regression_pipeline():

    pipeline = Pipeline([

        ("imputer", SimpleImputer(strategy="median")),

        ("selector", SelectKBest(
            score_func=mutual_info_regression
        )),

        ("model", GradientBoostingRegressor(
            random_state=42
        ))
    ])

    return pipeline


def train_regression_model(X_train, y_train):

    pipeline = build_regression_pipeline()

    grid = GridSearchCV(

        pipeline,

        param_grid={
            "selector__k": [10, 15, 20, 25, 30]
        },

        cv=5,

        scoring="neg_root_mean_squared_error",

        n_jobs=-1

    )

    grid.fit(X_train, y_train)

    return grid.best_estimator_