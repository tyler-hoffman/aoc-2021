from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Tuple

from src.day_09.models import Grid
from src.utils.point import Point


@dataclass
class Solver(ABC):
    grid: Grid

    @property
    @abstractmethod
    def solution(self) -> int:
        ...

    @property
    def low_points(self) -> List[Point]:
        points: List[Point] = []
        for y in range(self.grid.height):
            for x, level in enumerate(self.grid.levels[y]):
                point = Point(x=x, y=y)
                neighbors = self.neighbors(point)
                if all(
                    [level < self.grid.value_at(neighbor) for neighbor in neighbors]
                ):
                    points.append(point)
        return points

    def neighbors(self, point: Point) -> List[Point]:
        moves: List[Point] = [
            Point(x=0, y=1),
            Point(x=1, y=0),
            Point(x=0, y=-1),
            Point(x=-1, y=0),
        ]
        points = [p + point for p in moves]
        return [p for p in points if self.grid.value_at(p) is not None]
