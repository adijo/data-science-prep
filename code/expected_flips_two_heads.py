"""
Empirical evaluation of Question 2 -- `Flips until two heads`
(solved analytically in the pdf file)
"""
from common import bernoulli

ZERO, ONE, TWO = 0, 1, 2
BACKWARD, FORWARD = 0, 1


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
    total_steps = 0
    num_experiments = 50000
    for _ in range(num_experiments):
        total_steps += experiment(p=0.5)
    print(total_steps / num_experiments)


if __name__ == "__main__":
    main()
