from dataclasses import dataclass
from functools import cached_property
from typing import Dict, List
from src.day_07.parser import Parser
from src.day_07.solver import Solver
from src.utils.collections import frequency_map

@dataclass
class PositionInfo(object):
    crab_initial_positions: List[int]
    cost: int

class Day07PartBSolver(Solver):
    @property
    def solution(self) -> int:
        return min(self.position_costs.values())

    @cached_property
    def starting_frequencies(self) -> Dict[int, int]:
        return frequency_map(self.starting_positions)

    @cached_property
    def cost_map(self) -> Dict[int, int]:
        output = [0]
        for i in range(1, self.max_pos + 1):
            output.append(i + output[i - 1])
        return output

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
        return self._get_cost_in_direction(self.valid_positions_reversed, -1)

    @cached_property
    def right_move_costs(self) -> Dict[int, int]:
        return self._get_cost_in_direction(self.valid_positions, 1)

    def _get_cost_in_direction(self, positions: List[int], direction: int) -> Dict[int, int]:
        p = positions[0]
        start = PositionInfo(crab_initial_positions=[p]*self.starting_frequencies[p], cost=0)
        data: Dict[int, PositionInfo] = {
            positions[0]: start,
        }

        for p in positions[1:]:
            prev = data[p-direction]
            crabs_at_pos = self.starting_frequencies.get(p, 0)
            all_crabs = prev.crab_initial_positions + [p]*crabs_at_pos
            cost = sum([self.cost_map[abs(p - dist)] for dist in all_crabs])
            data[p] = PositionInfo(crab_initial_positions=all_crabs, cost=cost)

        return {p: d.cost for p, d in data.items()}

def solve(input: str) -> int:
    parser = Parser()
    solver = Day07PartBSolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_07/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
