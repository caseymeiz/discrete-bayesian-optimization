import pandas
import pandas as pd
from summit.guides.guide import Guide


class Criteria:
    def check(self, X, y):
        raise Exception("Implement")


def optimize(fn, guide: Guide, criteria: Criteria, domain: pd.DataFrame):
    X = pd.DataFrame(columns=domain.columns)
    y = pandas.DataFrame()

    while not criteria.check(X, y):
        x = guide.suggest(X, y, domain)
        fx = x.map(fn)
        X = pd.concat([X, x])
        y = pd.concat([y, fx])
