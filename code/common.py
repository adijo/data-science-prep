import numpy as np
from typing import List


def bernoulli(p: float) -> int:
    return np.random.binomial(1, p=p)


def reverse(a: List) -> List:
    return a[::-1]


def almost_equal(a: float, b: float, epsilon: float = 0.01) -> bool:
    return abs(a - b) < epsilon
