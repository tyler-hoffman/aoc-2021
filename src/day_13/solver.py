from dataclasses import dataclass
from functools import cached_property
from src.utils.point import Point
from src.day_13.models import Fold, FoldX, FoldY


@dataclass
class Folder(object):
    points: set[Point]
    folds: list[Fold]
    index: int = 0

    def fold_all(self):
        while self.index < self.fold_length:
            self.fold()
            self.index += 1

    def fold(self):
        match self.current_fold:
            case FoldX(value):
                for point in [p for p in self.points if p.x > value]:
                    self.points.add(Point(y=point.y, x=value - (point.x - value)))
                    self.points.remove(point)
            case FoldY(value):
                for point in [p for p in self.points if p.y > value]:
                    self.points.add(Point(x=point.x, y=value - (point.y - value)))
                    self.points.remove(point)

    def __repr__(self) -> str:
        output = ""
        for y in range(self.max_y + 1):
            for x in range(self.max_x + 1):
                if Point(x=x, y=y) in self.points:
                    output += "#"
                else:
                    output += " "
            output += "\n"
        return output

    @cached_property
    def fold_length(self) -> int:
        return len(self.folds)

    @property
    def current_fold(self) -> Fold:
        return self.folds[self.index]

    @property
    def max_x(self) -> int:
        return max([p.x for p in self.points])

    @property
    def max_y(self) -> int:
        return max([p.y for p in self.points])
