
class Guide:
    def suggest(self, X, y, domain):
        raise Exception("Implement")


class Criteria:
    def check(self, X, y):
        raise Exception("Implement")


def optimize(fn, guide: Guide, criteria: Criteria, domain):
    X = []
    y = []

    while not criteria.check(X, y):
        x = guide.suggest(X, y, domain)
        fx = fn(x)
        X.append(x)
        y.append(fx)
