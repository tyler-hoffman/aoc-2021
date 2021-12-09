from dataclasses import dataclass
from functools import cached_property
from typing import List


@dataclass
class Grid(object):
    levels: List[List[int]]

    @cached_property
    def width(self) -> int:
        return len(self.levels[0])

    @cached_property
    def height(self) -> int:
        return len(self.levels)
