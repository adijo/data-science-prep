"""
Empirical evaluation of Question 3 --`Drawing normally`
 (solved analytically in the pdf file)
"""

import numpy as np


def experiment():
    days = 0
    value = 0
    while value < 2:
        days += 1
        value = np.random.normal(0, 1)
    return days


def main():
    num_experiments = 100000
    total_days = 0
    for _ in range(num_experiments):
        total_days += experiment()
    print(total_days / num_experiments)


if __name__ == "__main__":
    main()
