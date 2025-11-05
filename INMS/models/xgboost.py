from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def get_model(random_state=42, **kwargs):
    steps = [
        ("xgb", XGBClassifier(
            random_state=random_state,
            eval_metric='logloss',
            **kwargs
        ))
    ]
    return Pipeline(steps)

# Expanded parameter grid with xgb__ prefix
param_grid = {
    'xgb__n_estimators': [100, 200, 300],
    'xgb__max_depth': [3, 6, 10],
    'xgb__learning_rate': [0.01, 0.05, 0.1, 0.2],
    'xgb__subsample': [0.7, 0.8, 0.9, 1.0],
    'xgb__colsample_bytree': [0.7, 0.8, 1.0],       # Feature sampling per tree
    'xgb__min_child_weight': [1, 3, 5],             # Minimum sum of weights in child
    'xgb__gamma': [0, 0.1, 0.2],                    # Minimum loss reduction for split
    'xgb__scale_pos_weight': [1, 10, 50]            # Balance for imbalanced classes
}