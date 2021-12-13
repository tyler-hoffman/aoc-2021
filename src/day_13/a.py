from dataclasses import dataclass
from src.day_13.models import Data, Fold, FoldX, FoldY
from src.day_13.parser import Parser
from src.day_13.solver import Solver
from src.utils.point import Point

@dataclass
class Folder(object):
    points: set[Point]
    folds: list[Fold]
    index: int = 0

    def fold(self):
        match self.current_fold:
            case FoldX(x):
                for point in [p for p in self.points if p.x > x]:
                    self.points.add(Point(y=point.y, x=x-(point.x-x)))
                    self.points.remove(point)
            case FoldY(y):
                for point in [p for p in self.points if p.x > y]:
                    self.points.add(Point(x=point.x, y=y-(point.y-y)))
                    self.points.remove(point)

    @property
    def current_fold(self) -> Fold:
        return self.folds[self.index]

@dataclass
class Day13PartASolver(Solver):
    data: Data

    @property
    def solution(self) -> int:
        folder = Folder(points=self.data.points, folds=self.data.folds)
        folder.fold()
        return len(folder.points)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day13PartASolver(data=data)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_13/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
