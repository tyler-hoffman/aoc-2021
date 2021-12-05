from typing import Optional
from src.day_04.parser import Parser
from src.day_04.solver import Solver, WinningState


class Day04PartBSolver(Solver):
    @property
    def solution(self) -> int:
        winning_state: Optional[WinningState] = None
        for state in self._winning_states:
            winning_state = state
        assert winning_state is not None
        return winning_state.score


def solve(input: str) -> int:
    parser = Parser()
    data = parser.parse(input)
    solver = Day04PartBSolver(boards=data.boards, draws=data.draws)
    return solver.solution


if __name__ == "__main__":
    with open("src/day_04/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
