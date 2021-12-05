import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property
from typing import Dict, List

from src.utils.line import Line
from src.utils.point import Point


@dataclass
class Solver(ABC):
    lines: List[Line]

    @property
    def solution(self):
        visits: Dict[Point, int] = {}
        for line in self.filtered_lines:
            for point in self._get_points_in_line(line):
                visits[point] = visits.get(point, 0) + 1

        return len([v for v in visits.values() if v > 1])

    @property
    @abstractmethod
    def filtered_lines(self) -> List[Line]:
        ...

    def _get_points_in_line(self, line: Line) -> List[Point]:
        a, b = line.a, line.b
        if line.is_horizontal:
            return self._get_points_between_horizontal(a, b)
        elif line.is_vertical:
            return self._get_points_between_vertical(a, b)
        else:
            return self._get_points_between_diagonal(a, b)

    def _get_points_between_horizontal(self, a: Point, b: Point) -> List[Point]:
        if b.x < a.x:
            a, b = b, a
        return [Point(x=x, y=a.y) for x in range(a.x, b.x + 1)]

    def _get_points_between_vertical(self, a: Point, b: Point) -> List[Point]:
        if b.y < a.y:
            a, b = b, a
        return [Point(x=a.x, y=y) for y in range(a.y, b.y + 1)]

    def _get_points_between_diagonal(self, a: Point, b: Point) -> List[Point]:
        if b.x < a.x:
            a, b = b, a
        if a.y < b.y:
            xs = range(a.x, b.x + 1)
            ys = range(a.y, b.y + 1)
            return [Point(x=x, y=y) for x, y in zip(xs, ys)]
        else:
            xs = range(a.x, b.x + 1)
            ys = range(a.y, b.y - 1, -1)
            return [Point(x=x, y=y) for x, y in zip(xs, ys)]


class Parser(object):
    @cached_property
    def regex_pattern(self) -> re.Pattern:
        return re.compile(r"\d+")

    def parse_line(self, line: str) -> Line:
        x1, y1, x2, y2 = [int(x) for x in self.regex_pattern.findall(line)]

        return Line(a=Point(x=x1, y=y1), b=Point(x=x2, y=y2))

    def parse(self, input: str) -> List[Line]:
        return [self.parse_line(line) for line in input.strip().splitlines()]
