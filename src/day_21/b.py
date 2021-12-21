from __future__ import annotations
from dataclasses import dataclass
from functools import cache, cached_property
from itertools import product
from src.day_21.parser import Parser
from src.day_21.solver import GameState, PlayerState
from src.utils.collections import frequency_map


@cache
def possible_rolls() -> list[int]:
    rolls = product(*[range(1, 4) for _ in range(3)])
    return [sum(r) for r in rolls]


@cache
def roll_frequencies() -> dict[int, int]:
    return frequency_map(possible_rolls())


@cache
def compute_win_count(state: GameState) -> tuple[int, int]:
    if state.player_a_won:
        return [1, 0]
    elif state.player_b_won:
        return [0, 1]
    else:
        a_wins = 0
        b_wins = 0
        for roll, freq in roll_frequencies().items():
            new_state = state.move(roll)
            new_a_wins, new_b_wins = compute_win_count(new_state)
            a_wins += freq * new_a_wins
            b_wins += freq * new_b_wins
        return a_wins, b_wins


@dataclass
class Day21PartBSolver(object):
    starts: tuple[int, int]

    @property
    def score_to_win(self) -> int:
        return 21

    @cached_property
    def solution(self) -> int:
        game_state = GameState(
            player_a=PlayerState(position=self.starts[0]),
            player_b=PlayerState(position=self.starts[1]),
            score_to_win=self.score_to_win,
        )
        win_counts = compute_win_count(game_state)
        return max(win_counts)


def solve(input: str) -> int:
    starts = Parser.parse(input)
    solver = Day21PartBSolver(starts=starts)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_21/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
