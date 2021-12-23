from dataclasses import dataclass
from src.day_23.models import GameState
from src.day_23.parser import Parser
from src.day_23.solver import Solver


@dataclass
class Day23PartASolver(Solver):
    start_state: GameState

    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    start_state = Parser.parse()
    solver = Day23PartASolver(start_state=start_state)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_23/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
