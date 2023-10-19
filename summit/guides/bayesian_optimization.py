import pandas as pd
from summit.guides.guide import Guide
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern


class BayesGuide(Guide):

    def __init__(self, kappa=2.5, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gp = GaussianProcessRegressor(kernel=Matern(nu=2.5))
        self.kappa = kappa

    def upper_confidence_bound(self, X: pd.DataFrame):
        mu, sigma = self.gp.predict(X, return_std=True)
        return mu + self.kappa * sigma

    def suggest(self, X: pd.DataFrame, y: pd.DataFrame, domain: pd.DataFrame) -> pd.DataFrame:
        if len(X) == 0:
            return domain.sample(1)
        self.gp.fit(X, y)
        ucb_values = pd.DataFrame(self.upper_confidence_bound(domain), index=domain.index)
        ucb_values = ucb_values[~ucb_values.index.isin(X.index)]
        return domain.iloc[ucb_values.idxmax()]
