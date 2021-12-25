from __future__ import annotations

from src.day_25.models import Bounds, State
from src.utils.point import Point


class Parser(object):
    @staticmethod
    def parse(input: str) -> State:
        east_cukes = set[Point]()
        south_cukes = set[Point]()

        lines = input.strip().splitlines()
        height = len(lines)
        width = len(lines[0])
        for y, line in enumerate(lines):
            for x, ch in enumerate(line):
                match ch:
                    case ">":
                        east_cukes.add(Point(x, y))
                    case "v":
                        south_cukes.add(Point(x, y))
                    case ".":
                        pass
                    case _:
                        raise Exception("Wat")
        return State(Bounds(width, height), east_cukes, south_cukes)
