import pandas as pd


class Guide:
    def __int__(self, priority: pd.DataFrame = None):
        self.priority = priority

    def suggest(self, X: pd.DataFrame, y: pd.DataFrame, domain: pd.DataFrame) -> pd.DataFrame:
        raise Exception("Implement")
