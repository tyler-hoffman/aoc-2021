import dataclasses
import re
from typing import List, Set


@dataclasses.dataclass
class Board(object):
    lines: List[List[int]]

    def has_match(self, items: Set[int]) -> bool:
        for i in range(5):
            if self.has_horizontal_match(items, i):
                return True
            elif self.has_vertical_match(items, i):
                return True

    def has_vertical_match(self, items: Set[int], x: int) -> bool:
        return all([self.lines[y][x] in items for y in range(5)])

    def has_horizontal_match(self, items: Set[int], y: int) -> bool:
        return all([self.lines[y][x] in items for x in range(5)])

    def unmarked_stuff(self, items: Set[int]) -> List[int]:
        output: List[int] = []

        for y in range(5):
            for x in range(5):
                thing = self.lines[y][x]
                if thing not in items:
                    output.append(thing)

        return output


@dataclasses.dataclass
class Data(object):
    boards: List[Board]
    picks: List[int]


def parse(input: str) -> Data:
    lines = input.strip().splitlines()

    picks = [int(x) for x in lines[0].split(",")]
    boards: List[Board] = []

    for index in range(2, len(lines), 6):
        board_data: List[List[int]] = []
        for line in lines[index : index + 5]:
            board_data.append([int(x) for x in re.split("\s+", line.strip())])
        boards.append(Board(lines=board_data))

    return Data(boards=boards, picks=picks)
