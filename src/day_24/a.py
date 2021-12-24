from dataclasses import dataclass
from src.day_24.models import Operator
from src.day_24.parser import Parser
from src.day_24.solver import Solver


@dataclass
class Day24PartASolver(Solver):
    instructions: list[Operator]

    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    instructions = Parser(input).parse()
    solver = Day24PartASolver(instructions=instructions)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_24/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
