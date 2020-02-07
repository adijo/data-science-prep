"""
Empirical evaluation of Question 2 (solved analytically in the pdf file)
"""

import numpy as np

ZERO, ONE, TWO = 0, 1, 2
BACKWARD, FORWARD = 0, 1


def bernoulli(p: float) -> int:
    return np.random.binomial(1, p=p)


def experiment(p: float) -> int:
    state = ZERO
    steps = 0
    while state != TWO:
        steps += 1
        if state == ZERO:
            state = ONE if bernoulli(p) == FORWARD else ZERO
        elif state == ONE:
            state = TWO if bernoulli(p) == FORWARD else ZERO
    return steps


def main():
    mean_steps = 0
    num_experiments = 50000
    for _ in range(num_experiments):
        mean_steps += experiment(p=0.5)
    print(mean_steps / num_experiments)


if __name__ == "__main__":
    main()
