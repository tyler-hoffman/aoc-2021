from __future__ import annotations
from dataclasses import dataclass
from functools import cache, cached_property
from itertools import product
from src.day_21.parser import Parser
from src.day_21.solver import GameState, Solver
from src.utils.collections import frequency_map


class Day21PartBSolver(Solver):
    @property
    def score_to_win(self) -> int:
        return 21

    @cached_property
    def solution(self) -> int:
        win_counts = self.compute_win_count(self.starting_state)
        return max(win_counts)

    @staticmethod
    @cache
    def compute_win_count(state: GameState) -> tuple[int, int]:
        if state.player_a_won:
            return [1, 0]
        elif state.player_b_won:
            return [0, 1]
        else:
            a_wins = 0
            b_wins = 0
            for roll, freq in Day21PartBSolver.roll_frequencies.items():
                new_state = state.move(roll)
                new_a_wins, new_b_wins = Day21PartBSolver.compute_win_count(new_state)
                a_wins += freq * new_a_wins
                b_wins += freq * new_b_wins
            return a_wins, b_wins

    @classmethod
    @property
    @cache
    def roll_frequencies(cls) -> dict[int, int]:
        return frequency_map(Day21PartBSolver.possible_rolls)

    @classmethod
    @property
    @cache
    def possible_rolls(cls) -> list[int]:
        rolls = product(*[range(1, 4) for _ in range(3)])
        return [sum(r) for r in rolls]


def solve(input: str) -> int:
    starts = Parser.parse(input)
    solver = Day21PartBSolver(starts=starts)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_21/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
