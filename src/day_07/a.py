from dataclasses import dataclass
from functools import cached_property
from typing import Dict, List
from src.day_07.parser import Parser
from src.day_07.solver import Solver
from src.utils.collections import frequency_map

@dataclass
class PositionInfo(object):
    crabs: int
    cost: int

class Day07PartASolver(Solver):

    @property
    def solution(self) -> int:
        return min(self.position_costs.values())

    @cached_property
    def starting_frequencies(self) -> Dict[int, int]:
        return frequency_map(self.starting_positions)

    @cached_property
    def min_pos(self) -> int:
        return min(self.starting_frequencies.keys())

    @cached_property
    def max_pos(self) -> int:
        return max(self.starting_frequencies.keys())

    @cached_property
    def valid_positions(self) -> List[int]:
        return list(range(self.min_pos, self.max_pos + 1))

    @cached_property
    def valid_positions_reversed(self) -> List[int]:
        return self.valid_positions[::-1]

    @cached_property
    def position_costs(self) -> Dict[int, int]:
        return {p: self.left_move_costs[p] + self.right_move_costs[p] for p in self.valid_positions}

    @cached_property
    def left_move_costs(self) -> Dict[int, int]:
        positions = self.valid_positions_reversed
        start = PositionInfo(cost=0, crabs=self.starting_frequencies[positions[0]])
        data: Dict[int, PositionInfo] = {
            positions[0]: start
        }

        for p in positions[1:]:
            prev = data[p+1]
            crabs_at_pos = self.starting_frequencies.get(p, 0)
            data[p] = PositionInfo(cost=prev.cost + prev.crabs, crabs=prev.crabs + crabs_at_pos)

        return {p: d.cost for p, d in data.items()}

    @cached_property
    def right_move_costs(self) -> Dict[int, int]:
        positions = self.valid_positions
        start = PositionInfo(cost=0, crabs=self.starting_frequencies[positions[0]])
        data: Dict[int, PositionInfo] = {
            positions[0]: start
        }

        for p in positions[1:]:
            prev = data[p-1]
            crabs_at_pos = self.starting_frequencies.get(p, 0)
            data[p] = PositionInfo(cost=prev.cost + prev.crabs, crabs=prev.crabs + crabs_at_pos)

        return {p: d.cost for p, d in data.items()}


def solve(input: str) -> int:
    parser = Parser()
    solver = Day07PartASolver(starting_positions=parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_07/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
