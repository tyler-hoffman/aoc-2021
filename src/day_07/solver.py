from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property
from typing import Dict, List

from src.utils.collections import frequency_map


@dataclass
class Solver(ABC):
    starting_positions: List[int]

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
    def position_costs(self) -> Dict[int, int]:
        return {
            p: self.sum_move_cost(p, self.starting_frequencies)
            for p in self.valid_positions
        }

    def sum_move_cost(self, position: int, positions_to_check: Dict[int, int]) -> int:
        output = 0
        for pos, freq in positions_to_check.items():
            output += freq * self.move_cost(abs(pos - position))
        return output

    @abstractmethod
    def move_cost(self, dist: int) -> int:
        ...
