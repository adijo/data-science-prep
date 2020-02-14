import numpy as np


def bernoulli(p: float) -> int:
    return np.random.binomial(1, p=p)
