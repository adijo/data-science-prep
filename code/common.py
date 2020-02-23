import numpy as np
from typing import List


def bernoulli(p: float) -> int:
    return np.random.binomial(1, p=p)


def reverse(a: List) -> List:
    return a[::-1]
