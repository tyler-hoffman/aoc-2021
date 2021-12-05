from typing import List
from src.day_05.shared import Parser, Solver
from src.utils.line import Line


class Day05PartASolver(Solver):
    @property
    def filtered_lines(self) -> List[Line]:
        return [line for line in self.lines if line.is_horizontal or line.is_vertical]


def solve(input: str) -> int:
    parser = Parser()
    solver = Day05PartASolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_05/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
