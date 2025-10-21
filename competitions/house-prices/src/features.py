# Feature engineering stubs
# Implement transform classes with fit/transform to avoid leakage.
class FeaturePipeline:
    def __init__(self, steps=None):
        self.steps = steps or []

    def fit(self, df):
        for step in self.steps:
            if hasattr(step, 'fit'):
                step.fit(df)
        return self

    def transform(self, df):
        out = df.copy()
        for step in self.steps:
            out = step.transform(out)
        return out
