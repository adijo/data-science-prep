import numpy as np
from typing import List
from common import almost_equal


def correlation(x: List[int], y: List[int]) -> float:

    assert len(x) == len(y)

    n = len(x)
    x_mean, y_mean = np.mean(x), np.mean(y)
    x_std_dev, y_std_dev = np.std(x), np.std(y)

    numerator = sum([x_i * y_i for (x_i, y_i) in zip(x, y)]) - (n * x_mean * y_mean)
    denominator = n * x_std_dev * y_std_dev
    return numerator / denominator


a, b = [0, 14, 1, 10, 5], [2, 6, 8, 5, 6]
assert almost_equal(correlation(a, b), np.corrcoef(a, b)[0][1])
