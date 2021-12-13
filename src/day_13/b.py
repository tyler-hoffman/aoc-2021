from dataclasses import dataclass
from src.day_13.models import Data
from src.day_13.parser import Parser
from src.day_13.solver import Folder
from src.services.human_service import HumanService


@dataclass
class Day13PartBSolver(object):
    data: Data

    @property
    def solution(self) -> str:
        folder = Folder(points=self.data.points, folds=self.data.folds)
        folder.fold_all()

        return str(folder)


def solve(input_string: str, human_service: HumanService) -> int:
    data = Parser.parse(input_string)
    solver = Day13PartBSolver(data=data)

    human_readable = solver.solution
    human_service.say(human_readable)
    aoc_readable = human_service.ask("What's that look like to you?")

    return aoc_readable


if __name__ == "__main__":
    with open("src/day_13/input.txt", "r") as f:
        input_string = f.read()
    print(solve(input_string, HumanService()))
