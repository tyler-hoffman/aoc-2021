from dataclasses import dataclass
from src.day_25.models import State
from src.day_25.parser import Parser
from src.day_25.solver import Solver


@dataclass
class Day25PartASolver(Solver):
    start_state: State

    @property
    def solution(self) -> int:
        state = self.start_state
        count = 0
        while state:
            count += 1
            state = state.next_state()
        return count


def solve(input: str) -> int:
    state = Parser.parse(input)
    solver = Day25PartASolver(start_state=state)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_25/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
