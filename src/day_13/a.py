from dataclasses import dataclass
from src.day_13.models import Data
from src.day_13.parser import Parser
from src.day_13.solver import Folder


@dataclass
class Day13PartASolver(object):
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
