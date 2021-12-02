from __future__ import annotations
import dataclasses
from typing import Any


@dataclasses.dataclass(frozen=True)
class Point(object):
    x: int
    y: int

    def __add__(self, other: Any) -> Point:
        if isinstance(other, Point):
            return Point(x=self.x + other.x, y=self.y + other.y)
        else:
            raise Exception(f"Point cannot be added with {type(other)}")
