import math
import random
from dataclasses import dataclass

from scipy.spatial import distance


@dataclass
class Point:
    x: float
    y: float


def euclidean_distance(a: Point, b: Point) -> float:
    return distance.euclidean((a.x, a.y), (b.x, b.y))


def is_inside_circle(a: Point) -> bool:
    return euclidean_distance(a, Point(0.5, 0.5)) < 0.5


def simulate(n_iter: int) -> float:

    num_points_within_circle: int = sum(
        [
            1 if is_inside_circle(Point(x=random.random(), y=random.random())) else 0
            for _ in range(n_iter)
        ]
    )

    return (float(num_points_within_circle) / n_iter) * 4


epsilon = 0.01
assert (simulate(100000) - math.pi) < epsilon
