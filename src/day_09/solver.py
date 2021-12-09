from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Tuple

from src.day_09.models import Grid


@dataclass
class Solver(ABC):
    grid: Grid

    @property
    @abstractmethod
    def solution(self) -> int:
        ...

    @property
    def low_points(self) -> List[Tuple[int, int]]:
        points: List[int] = []
        for y in range(self.grid.height):
            for x, level in enumerate(self.grid.levels[y]):
                neighbors = self.neighbors(x, y)
                if all([level < self.grid.value_at(x, y) for x, y in neighbors]):
                    points.append((x, y))
        return points

    def neighbors(self, x: int, y: int) -> List[int]:
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        return [
            (x + a, y + b)
            for a, b in moves
            if self.grid.value_at(x + a, y + b) is not None
        ]
