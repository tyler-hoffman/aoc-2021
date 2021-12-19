from dataclasses import dataclass
from functools import cached_property
from itertools import permutations
from src.day_18.parser import Parser
from src.day_18.solver import SnailfishNumber


@dataclass
class Day18PartBSolver(object):
    snailfish_numbers: list[SnailfishNumber]

    @cached_property
    def solution(self) -> int:
        return max(self.possible_magnitudes)

    @cached_property
    def possible_magnitudes(self) -> set[int]:
        pairs = permutations(self.snailfish_numbers, 2)
        sums = [self.deep_copy(a) + self.deep_copy(b) for a, b in pairs]
        return {x.magnitude for x in sums}

    def deep_copy(self, snailfish_number: SnailfishNumber) -> SnailfishNumber:
        """Make a deep copy of a snailfish number

        It'd probably be more "correct" to make this a method on the SnailfishNumber,
        which I don't want importing the parser. But this is pretty easy, so we're
        just copying by serializing/deserializing.
        """
        s = str(snailfish_number)
        return Parser.parse_snailfish_number(s)


def solve(input: str) -> int:
    snailfish_numbers = Parser.parse_all(input)
    solver = Day18PartBSolver(snailfish_numbers=snailfish_numbers)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_18/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
