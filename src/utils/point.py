from __future__ import annotations
import dataclasses
from functools import cached_property, total_ordering
from typing import Any


@total_ordering
@dataclasses.dataclass(frozen=True)
class Point(object):
    x: int
    y: int

    @cached_property
    def magnitude(self) -> int:
        return abs(self.x) + abs(self.y)

    def __lt__(self, other) -> bool:
        if isinstance(other, Point):
            return self.magnitude < other.magnitude
        else:
            raise Exception(f"You can't compare {other} to a Point!")

    def __add__(self, other: Any) -> Point:
        if isinstance(other, Point):
            return Point(x=self.x + other.x, y=self.y + other.y)
        else:
            raise Exception(f"Point cannot be added with {type(other)}")
