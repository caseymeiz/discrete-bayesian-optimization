from summit.optimize import optimize, Guide, Criteria
import pandas as pd


def main():
    guide = SkeletonGuide()
    criteria = SkeletonCriteria()
    domain = pd.DataFrame(dict(x=[1, 2, 3, 4]))
    fn = lambda x: x ** 2

    optimize(fn, guide, criteria, domain)


class SkeletonGuide(Guide):
    def suggest(self, X, y, domain: pd.DataFrame):
        return domain.sample(1)


class SkeletonCriteria(Criteria):
    def check(self, X, y):
        if len(y) == 0:
            return False
        return y[-1].iloc[0, 0] > 5


if __name__ == "__main__":
    main()
