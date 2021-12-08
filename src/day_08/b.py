from dataclasses import dataclass
from functools import cache, cached_property
from typing import Dict, List, Optional
from src.day_08.models import Chunk, Entry
from src.day_08.parser import Parser
from src.day_08.solver import NumberInfo, Solver


class Day08PartBSolver(Solver):
    @property
    def solution(self) -> int:
        line_solvers = [LineSolver(entry) for entry in self.entries]
        return sum([solver.solution for solver in line_solvers])


@dataclass
class LineSolver(object):
    entry: Entry

    @property
    def solution(self) -> int:
        numbers = [self.chunks_to_ints[x] for x in self.entry.output_value]
        return self.number_array_to_number(numbers)

    @cached_property
    def chunks_to_ints(self) -> Dict[Chunk, int]:
        return {
            self.zero: 0,
            self.one: 1,
            self.two: 2,
            self.three: 3,
            self.four: 4,
            self.five: 5,
            self.six: 6,
            self.seven: 7,
            self.eight: 8,
            self.nine: 9,
        }

    @staticmethod
    def number_array_to_number(numbers: List[int]) -> int:
        output = 0
        for i, x in enumerate(numbers[::-1]):
            output += x * 10 ** i
        return output

    def find_chunks_by_length(self, length: int) -> List[Chunk]:
        return [x for x in self.entry.signal_patterns if len(x) == length]

    def find_chunk_if_simple(self, value: int) -> Optional[Chunk]:
        """
        Attempt to find the chunk for a value based on its
        expected length alone. e.g. 1 is the only number with 2 segments,
        so we can find the right chunk. If we can't, return None
        """
        if not NumberInfo.can_determine_value_by_length(value):
            return None

        outputs = self.find_chunks_by_length(NumberInfo.value_length(value))
        assert len(outputs) == 1
        return outputs[0]

    # Now for the ugly part...
    # We have a property for each number.
    # Some are easy to figure out (i.e. 1, 4, 7, 8)
    # Some use the idea of erasing segments from a digit display where another
    #    digit display would would cover those segmens. e.g. we find 9 because
    #    it is the only number that would completely cover 4.
    #    so for each chunk that could potentially be 9, we subtract its segments
    #    from the segments for 4, and if we have nothing left, we found our 9.
    # Some use process of elimination.
    #  - e.g. we find 2 because it has 5 segments and it isn't 5 or 3

    @cached_property
    def zero(self) -> str:
        options = self.find_chunks_by_length(6)
        filtered = [x for x in options if x not in (self.six, self.nine)]
        assert len(filtered) == 1
        return filtered[0]

    @cached_property
    def one(self) -> str:
        return self.find_chunk_if_simple(1)

    @cached_property
    def two(self) -> str:
        options = self.find_chunks_by_length(5)
        filtered = [x for x in options if x not in (self.five, self.three)]
        assert len(filtered) == 1
        return filtered[0]

    @cached_property
    def three(self) -> str:
        options = self.find_chunks_by_length(5)
        filtered = [x for x in options if len(self.one - x) == 0]
        assert len(filtered) == 1
        return filtered[0]

    @cached_property
    def four(self) -> str:
        return self.find_chunk_if_simple(4)

    @cached_property
    def five(self) -> str:
        options = self.find_chunks_by_length(5)
        filtered = [x for x in options if len(self.six - x) == 1]
        assert len(filtered) == 1
        return filtered[0]

    @cached_property
    def six(self) -> str:
        options = self.find_chunks_by_length(6)
        filtered = [x for x in options if len(self.one - x) == 1]
        assert len(filtered) == 1
        return filtered[0]

    @cached_property
    def seven(self) -> str:
        return self.find_chunk_if_simple(7)

    @cached_property
    def eight(self) -> str:
        return self.find_chunk_if_simple(8)

    @cached_property
    def nine(self) -> str:
        options = self.find_chunks_by_length(6)
        filtered = [x for x in options if len(self.four - x) == 0]
        assert len(filtered) == 1
        return filtered[0]


def solve(input: str) -> int:
    parser = Parser()
    solver = Day08PartBSolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_08/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
