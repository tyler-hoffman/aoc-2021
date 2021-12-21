from functools import cached_property
from typing import Iterator
from src.day_21.parser import Parser
from src.day_21.solver import Solver


class Day21PartASolver(Solver):
    @property
    def score_to_win(self) -> int:
        return 1000

    @cached_property
    def solution(self) -> int:
        game_state = self.starting_state
        roll_count = 0
        rolls = self.rolls()
        while not game_state.won:
            to_move = sum([next(rolls) for _ in range(3)])
            game_state = game_state.move(to_move)
            roll_count += 3

        if game_state.player_a_won:
            return game_state.player_b.score * roll_count
        else:
            return game_state.player_a.score * roll_count

    def rolls(self) -> Iterator[int]:
        x = 0
        while True:
            yield x + 1
            x += 1
            x %= 100


def solve(input: str) -> int:
    starts = Parser.parse(input)
    solver = Day21PartASolver(starts=starts)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_21/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
