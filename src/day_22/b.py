from functools import cached_property
from src.day_22.models import Instruction
from src.day_22.parser import Parser
from src.day_22.solver import Solver


class Day22PartBSolver(Solver):
    @cached_property
    def bounded_instructions(self) -> list[Instruction]:
        # no bounds babyyyyyy
        return self.instructions


def solve(input: str) -> int:
    parser = Parser()
    solver = Day22PartBSolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_22/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
