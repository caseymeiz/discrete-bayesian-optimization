import math
import pandas as pd
import plotly.graph_objects as go
from summit.optimize import optimize, Criteria
from summit.guides.bayesian_optimization import BayesGuide


def main():
    guide = BayesGuide()
    criteria = SkeletonCriteria()
    domain = pd.DataFrame(dict(x=list(range(100))))
    fn = lambda x: (math.sin((math.pi * (x - 20)) / 50) + math.cos((1.5 * math.pi * (x - 20)) / 50)) * 20

    optimize(fn, guide, criteria, domain)


    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=domain.x,
            y=domain.map(fn).x
        )
    )
    fig.show()


class SkeletonCriteria(Criteria):
    def check(self, X, y):
        if len(y) == 0:
            return False
        return any(y.x > 20)


if __name__ == "__main__":
    main()
