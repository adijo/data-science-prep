import matplotlib.pyplot as plt
import seaborn as sns

from common import bernoulli

sns.set(style="darkgrid")

HEADS, TAILS = 1, 0


def experiment(p: float) -> int:
    while True:
        flips = [bernoulli(p), bernoulli(p)]
        if sum(flips) == 1:
            # HT means H and TH means T
            return HEADS if flips[0] == 1 and flips[1] == 0 else TAILS


def main():
    num_experiments = 100000
    num_heads = 0
    p: float = 0.7
    for _ in range(num_experiments):
        if experiment(p) == HEADS:
            num_heads += 1
    print("Number of heads", num_heads)
    print("Number of tails", num_experiments - num_heads)
    plt.bar(["heads", "tails"], [num_heads, num_experiments - num_heads])
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
