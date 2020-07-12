import math
import random
from dataclasses import dataclass
from typing import ClassVar, Generator

from common import almost_equal

from scipy.spatial import distance


@dataclass
class Point:
    x: float
    y: float


def euclidean_distance(a: Point, b: Point) -> float:
    return distance.euclidean((a.x, a.y), (b.x, b.y))


class UnitCircle:
    center: ClassVar[Point] = Point(0.5, 0.5)
    radius: ClassVar[float] = 0.5

    def contains(self, point: Point) -> bool:
        return euclidean_distance(point, self.center) < self.radius


def simulate(n_iter: int) -> float:
    unit_circle = UnitCircle()
    random_points: Generator[Point] = (Point(x=random.random(), y=random.random()) for _ in range(n_iter))
    num_points_within_circle: int = sum(
        [1 if unit_circle.contains(point) else 0 for point in random_points]
    )

    return (float(num_points_within_circle) / n_iter) * 4


assert almost_equal(simulate(100000), math.pi)
