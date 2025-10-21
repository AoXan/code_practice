# Utility helpers (logging, seed control, paths)
import os, random, numpy as np

def set_seed(seed: int = 42):
    import torch
    random.seed(seed)
    np.random.seed(seed)
    try:
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    except Exception:
        pass

def ensure_dir(p):
    os.makedirs(p, exist_ok=True)
