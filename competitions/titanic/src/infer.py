# Inference skeleton
import pandas as pd
def infer(models, X_te, proba=True):
    import numpy as np
    preds = []
    for m in models:
        p = getattr(m, "predict_proba", m.predict)(X_te)
        if proba and p.ndim == 2:
            p = p[:, 1]
        preds.append(p)
    return pd.Series(sum(preds) / len(preds), index=X_te.index)
