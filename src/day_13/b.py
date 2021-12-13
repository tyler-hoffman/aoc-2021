from dataclasses import dataclass
from src.day_13.models import Data
from src.day_13.parser import Parser
from src.day_13.solver import Folder, Solver

@dataclass
class Day13PartBSolver(Solver):
    data: Data

    @property
    def solution(self) -> str:
        folder = Folder(points=self.data.points, folds=self.data.folds)
        folder.fold_all()

        print(folder.get_str())
        answer = input("What number is that? ")

        return answer


def solve(input_string: str) -> int:
    data = Parser.parse(input_string)
    solver = Day13PartBSolver(data=data)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_13/input.txt", "r") as f:
        input_string = f.read()
    print(solve(input_string))
