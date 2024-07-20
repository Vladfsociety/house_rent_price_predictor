import numpy as np
from sklearn.ensemble import VotingRegressor


class IntervalVotingRegressor(VotingRegressor):
    def __init__(self, estimators, weights=None, n_jobs=None, verbose=False, interval_width=0.95):
        self.interval_width = interval_width
        self.lower_quantile = (1 - self.interval_width) / 2
        self.upper_quantile = 1 - self.lower_quantile
        super().__init__(estimators=estimators, weights=weights, n_jobs=n_jobs, verbose=verbose)

    def fit(self, X, y):
        super().fit(X, y)

        y_pred = super().predict(X)
        self.residuals = y - y_pred

        return self

    def predict(self, X):
        y_pred = super().predict(X)

        lower_bound = y_pred + np.quantile(self.residuals, self.lower_quantile)
        upper_bound = y_pred + np.quantile(self.residuals, self.upper_quantile)

        return np.column_stack((lower_bound, y_pred, upper_bound))