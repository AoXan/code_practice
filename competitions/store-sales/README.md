# Store Sales - Time Series Forecasting

**Kaggle Link**: https://www.kaggle.com/competitions/store-sales-time-series-forecasting  
**Primary Metric**: <fill in>  
**Goal (This Week)**: Reach a stable CV and 1–2 meaningful submissions. Target public LB: <fill in>.

## Quick Start
```bash
# inside this folder
make -f ../../templates/Makefile download COMP=store-sales
unzip -d data/ data/store-sales.zip
```

Then work in `notebooks/`:
- `eda.ipynb` — data overview and basic baseline
- `train_cv.ipynb` — cross-validated training pipeline
- `inference.ipynb` — deterministic inference and submission
