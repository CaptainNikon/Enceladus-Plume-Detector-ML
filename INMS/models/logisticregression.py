from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import numpy as np

def get_model(random_state=42, **kwargs):
    steps = [
        ("scaler", StandardScaler()),
        ("logreg", LogisticRegression(random_state=random_state, **kwargs))
    ]
    return Pipeline(steps)


param_grid = {
    'logreg__C': np.logspace(-4, 2, 15),  # From 1e-4 to 1e2 (15 steps)
    'logreg__penalty': ['l2'],
    'logreg__solver': ['newton-cholesky'],
    'logreg__max_iter': [500, 1000, 2000,5000],
    'logreg__class_weight': ['balanced',None]
}