from dataclasses import dataclass
from functools import cached_property
from typing import List, Optional


@dataclass
class Grid(object):
    levels: List[List[int]]

    @cached_property
    def width(self) -> int:
        return len(self.levels[0])

    @cached_property
    def height(self) -> int:
        return len(self.levels)

    def value_at(self, x: int, y: int) -> Optional[int]:
        if all(
            [
                y >= 0,
                y < self.height,
                x >= 0,
                x < self.width,
            ]
        ):
            return self.levels[y][x]
        else:
            return None
