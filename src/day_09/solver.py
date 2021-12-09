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
                neighbors = self.grid.neighbors(point)
                if all(
                    [level < self.grid.value_at(neighbor) for neighbor in neighbors]
                ):
                    points.append(point)
        return points
