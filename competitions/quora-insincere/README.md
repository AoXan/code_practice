# Quora Insincere Questions Classification

**Kaggle Link**: https://www.kaggle.com/c/quora-insincere-questions-classification  
**Primary Metric**: <fill in>  
**Goal (This Week)**: Reach a stable CV and 1–2 meaningful submissions. Target public LB: <fill in>.

## Quick Start
```bash
# inside this folder
make -f ../../templates/Makefile download COMP=quora-insincere
unzip -d data/ data/quora-insincere.zip
```

Then work in `notebooks/`:
- `eda.ipynb` — data overview and basic baseline
- `train_cv.ipynb` — cross-validated training pipeline
- `inference.ipynb` — deterministic inference and submission
