from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def get_model(random_state=42, **kwargs):
    steps = [
        ("scaler", StandardScaler()),
        ("knn", KNeighborsClassifier(**kwargs))
    ]
    return Pipeline(steps)


param_grid = {
    'knn__n_neighbors': [1,3, 5, 7, 9, 11,13,15,17],
    'knn__weights': ['uniform', 'distance'], 
    'knn__metric': ['euclidean', 'manhattan'],
    'knn__algorithm': ['auto'],
    'knn__leaf_size': [10,20, 30, 40, 50, 60],
}

