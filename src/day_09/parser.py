from typing import List

from src.day_09.models import Grid


class Parser(object):
    def parse(self, input: str) -> Grid:
        lines = [self.parse_line(line) for line in input.strip().splitlines()]
        return Grid(levels=lines)

    def parse_line(self, line: str) -> List[int]:
        return [int(x) for x in line]
