from dataclasses import dataclass
from functools import cached_property
from typing import List, Optional

from src.utils.point import Point


@dataclass
class Grid(object):
    levels: List[List[int]]

    @cached_property
    def width(self) -> int:
        return len(self.levels[0])

    @cached_property
    def height(self) -> int:
        return len(self.levels)

    def value_at(self, point: Point) -> Optional[int]:
        if all(
            [
                point.y >= 0,
                point.y < self.height,
                point.x >= 0,
                point.x < self.width,
            ]
        ):
            return self.levels[point.y][point.x]
        else:
            return None

    def neighbors(self, point: Point) -> List[Point]:
        moves: List[Point] = [
            Point(x=0, y=1),
            Point(x=1, y=0),
            Point(x=0, y=-1),
            Point(x=-1, y=0),
        ]
        points = [p + point for p in moves]
        return [p for p in points if self.value_at(p) is not None]
