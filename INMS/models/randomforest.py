from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def get_model(random_state=42, **kwargs):
    steps = [ 
        ("rf", RandomForestClassifier(random_state=random_state, **kwargs))
    ]
    return Pipeline(steps)

param_grid = {
    'rf__n_estimators': [50, 100, 200],
    'rf__max_depth': [5,6,7,8,9, 10,11,12],
    'rf__min_samples_split': [2, 5],
    'rf__min_samples_leaf': [1, 2],
    'rf__max_features': ['sqrt', 'log2'],
    'rf__class_weight': ['balanced', None]
}