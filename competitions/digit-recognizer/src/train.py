# Cross-validated training skeleton (tabular example)
import pandas as pd
from sklearn.model_selection import StratifiedKFold, KFold
from sklearn.metrics import accuracy_score, mean_squared_error

def train_cv(X, y, model_builder, n_splits=5, stratify=True, random_state=42):
    kf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=random_state) if stratify else KFold(n_splits=n_splits, shuffle=True, random_state=random_state)
    oof = pd.Series(index=X.index, dtype=float)
    models = []
    for fold, (trn_idx, val_idx) in enumerate(kf.split(X, y)):
        X_tr, X_va = X.iloc[trn_idx], X.iloc[val_idx]
        y_tr, y_va = y.iloc[trn_idx], y.iloc[val_idx]
        model = model_builder()
        model.fit(X_tr, y_tr)
        pred = getattr(model, "predict_proba", model.predict)(X_va)
        if pred.ndim == 2:
            pred = pred[:, 1]
        oof.iloc[val_idx] = pred
        models.append(model)
        # TODO: compute metric
    return models, oof
