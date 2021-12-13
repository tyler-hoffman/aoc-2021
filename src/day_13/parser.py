from typing import List
from src.day_13.models import Data, Fold, FoldX, FoldY

from src.utils.point import Point


class Parser(object):
    @classmethod
    def parse_point(cls, line: str) -> Point:
        x, y = line.split(",")
        return Point(x=int(x), y=int(y))

    @classmethod
    def parse_fold(cls, line: str) -> Point:
        _, last_part = line.split("=")
        if "x=" in line:
            return FoldX(value=int(last_part))
        elif "y=" in line:
            return FoldY(value=int(last_part))
        else:
            raise Exception("Invalid fold line: {line}")

    @classmethod
    def parse(cls, input: str) -> Data:
        done_with_points = False
        points = set[Point]()
        folds = list[Fold]()

        for line in input.strip().splitlines():
            if not line.strip():
                done_with_points = True
            elif not done_with_points:
                points.add(cls.parse_point(line))
            else:
                folds.append(cls.parse_fold(line))

        return Data(points=points, folds=folds)

