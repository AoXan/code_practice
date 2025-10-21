# Leakage Checklist
- [ ] Train-only statistics for scaling/encoding
- [ ] No future-looking features in time series (use lag/rolling with care)
- [ ] Group-based split when entities repeat across folds
- [ ] Remove identifier proxies (e.g., row IDs embedded in features)
- [ ] Re-check after feature engineering
