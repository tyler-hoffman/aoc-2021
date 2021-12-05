from src.day_04.parser import parse
from src.day_04.solver import Solver


class Day04PartASolver(Solver):
    @property
    def solution(self) -> int:
        winning_state = next(self._winning_states)
        return winning_state.score


def solve(input: str) -> int:
    data = parse(input)
    solver = Day04PartASolver(boards=data.boards, draws=data.draws)
    return solver.solution


if __name__ == "__main__":
    with open("src/day_04/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
