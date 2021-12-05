import re
from functools import cached_property
from typing import List

from src.utils.line import Line
from src.utils.point import Point


class Parser(object):
    @cached_property
    def regex_pattern(self) -> re.Pattern:
        return re.compile(r"\d+")

    def parse_line(self, line: str) -> Line:
        x1, y1, x2, y2 = [int(x) for x in self.regex_pattern.findall(line)]

        return Line(a=Point(x=x1, y=y1), b=Point(x=x2, y=y2))

    def parse(self, input: str) -> List[Line]:
        return [self.parse_line(line) for line in input.strip().splitlines()]
