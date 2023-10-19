import pandas as pd
from summit.guides.guide import Guide


class RandomGuide(Guide):
    def suggest(self, X: pd.DataFrame, y: pd.DataFrame, domain: pd.DataFrame) -> pd.DataFrame:
        return domain[~domain.index.isin(X.index)].sample(1)
