from random import sample
from common import almost_equal


def experiment(total_shows: int, num_top_shows: int):
    shows = range(total_shows)
    alice = sample(shows, num_top_shows)
    bob = sample(shows, num_top_shows)
    return len(set(alice) & set(bob))


def simulate(n_experiments=1000000):
    count = 0
    for i in range(n_experiments):
        count += experiment(total_shows=50, num_top_shows=3)
    return float(count) / n_experiments


assert almost_equal(simulate(), 0.18)
