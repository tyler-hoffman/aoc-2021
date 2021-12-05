from dataclasses import dataclass
from typing import List, Set


@dataclass(frozen=True)
class Board(object):
    lines: List[List[int]]

    def wins(self, items: Set[int]) -> bool:
        for i in range(5):
            if self.has_horizontal_win(items, i):
                return True
            elif self.has_vertical_win(items, i):
                return True

    def has_vertical_win(self, items: Set[int], x: int) -> bool:
        return all([self.lines[y][x] in items for y in range(5)])

    def has_horizontal_win(self, items: Set[int], y: int) -> bool:
        return all([self.lines[y][x] in items for x in range(5)])

    def unmarked_stuff(self, items: Set[int]) -> List[int]:
        output: List[int] = []

        for y in range(5):
            for x in range(5):
                thing = self.lines[y][x]
                if thing not in items:
                    output.append(thing)

        return output
