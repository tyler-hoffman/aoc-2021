import re
from functools import cached_property
from typing import List

from src.utils.line import Line
from src.utils.point import Point


def get_points_in_line(line: Line) -> List[Point]:
    a, b = line.a, line.b
    if line.is_horizontal:
        if b.x < a.x:
            a,b=b,a

        return [Point(x=x, y=a.y) for x in range(a.x, b.x + 1)]
    elif line.is_vertical:
        if b.y < a.y:
            a,b=b,a
        return [Point(x=a.x, y=y) for y in range(a.y, b.y + 1)]
    else:
        raise Exception("Diagonal line detected!")

class Parser(object):

    @cached_property
    def regex_pattern(self) -> re.Pattern:
        return re.compile(r"\d+")

    def parse_line(self, line: str) -> Line:
        x1, y1, x2, y2 = [int(x) for x in self.regex_pattern.findall(line)]

        return Line(a=Point(x=x1, y=y1), b=Point(x=x2, y=y2))

    def parse(self, input: str) -> List[Line]:
        return [self.parse_line(line) for line in input.strip().splitlines()]
