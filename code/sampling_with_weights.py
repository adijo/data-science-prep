"""
Sampling with weights: Lyft
Say we are given a list of several categories
(for example, the strings: A, B, C, and D) and want to sample from a
list of such categories according to a particular weighting scheme.
Such an example would be: for 100 items total,
we want to see A 20% of the time, B 15% of the time, C 35% of the time,
and D 30% of the time. How do we simulate this?
What if we care about an arbitrary number of categories and about memory usage?
"""

from typing import Dict, Callable, Tuple
import random
import matplotlib.pyplot as plt


def sample_weights_inefficient(categories: Dict[str, int], num_items: int) -> Callable:
    items = list()
    for category, percentage in categories.items():
        num_items_for_category = [category] * round((percentage / num_items) * 100)
        items.extend(num_items_for_category)

    def sampler() -> str:
        return random.choice(items)

    return sampler


def assign_ranges(
    categories: Dict[str, int], num_items: int
) -> Dict[Tuple[int, int], str]:
    low = 1
    ranges = dict()
    for category, percentage in categories.items():
        num_items_for_category = round((percentage / num_items) * 100)
        ranges[(low, low + num_items_for_category - 1)] = category
        low = low + num_items_for_category
    return ranges


def sample_weights_efficient(categories: Dict[str, int], num_items: int) -> Callable:
    assert sum(categories.values()) == 100
    ranges = assign_ranges(categories, num_items)

    def sampler() -> str:
        random_int = random.randrange(1, 101)
        for (low, high), category in ranges.items():
            if low <= random_int <= high:
                return category

    return sampler


def empirical_test(sampler: Callable, num_samples: int) -> Dict[str, float]:
    samples = dict()
    for _ in range(num_samples):
        sample = sampler()
        samples[sample] = samples.get(sample, 0) + 1
    return {key: float(value) / num_samples for key, value in samples.items()}


def main():
    categories = {"A": 20, "B": 15, "C": 35, "D": 30}

    sampler_one = sample_weights_inefficient(categories=categories, num_items=100)

    sampler_two = sample_weights_efficient(categories=categories, num_items=100)

    test_one = empirical_test(sampler_one, 10000)
    test_two = empirical_test(sampler_two, 10000)

    x_axis = test_one.keys()

    plt.bar(x_axis, [test_one[x] for x in x_axis])
    plt.show()
    plt.bar(x_axis, [test_two[x] for x in x_axis])
    plt.show()


if __name__ == "__main__":
    main()
