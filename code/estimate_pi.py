import math
import random
from dataclasses import dataclass
from common import almost_equal

from scipy.spatial import distance


@dataclass
class Point:
    x: float
    y: float


def euclidean_distance(a: Point, b: Point) -> float:
    return distance.euclidean((a.x, a.y), (b.x, b.y))


def is_inside_circle(point: Point) -> bool:
    circle_center = Point(0.5, 0.5)
    circle_radius = 0.5
    return euclidean_distance(point, circle_center) < circle_radius


def simulate(n_iter: int) -> float:
    random_points = (Point(x=random.random(), y=random.random()) for _ in range(n_iter))
    num_points_within_circle: int = sum(
        [1 if is_inside_circle(point) else 0 for point in random_points]
    )

    return (float(num_points_within_circle) / n_iter) * 4


assert almost_equal(simulate(100000), math.pi)
