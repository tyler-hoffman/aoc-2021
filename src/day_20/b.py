from more_itertools import nth
from src.day_20.parser import Parser
from src.day_20.solver import Solver


class Day20PartBSolver(Solver):
    @property
    def solution(self) -> int:
        image = nth(self.enhancements(), 50)
        return len(image.pixels)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day20PartBSolver(algorithm=data.algorithm, input_image=data.image)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_20/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
