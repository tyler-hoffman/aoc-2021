from dataclasses import dataclass
from functools import cached_property
from src.day_21.parser import Parser
from src.day_21.solver import Dice, Solver


@dataclass
class DeterministicDice(Dice):
    current_value: int = -1

    def next_roll(self) -> int:
        self.current_value += 1
        self.current_value %= 100
        return self.current_value + 1


class Day21PartASolver(Solver):
    @cached_property
    def dice(self) -> Dice:
        return DeterministicDice()


def solve(input: str) -> int:
    starts = Parser.parse(input)
    solver = Day21PartASolver(starts=starts)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_21/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
