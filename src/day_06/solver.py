from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Iterator, List

from src.utils.collections import frequency_map


@dataclass
class Solver(ABC):
    starting_values: List[int]
    days: int

    @property
    @abstractmethod
    def solution(self) -> int:
        ...

    def _frequencies_at_days(self) -> Iterator[Dict[int, int]]:
        freqs = frequency_map(self.starting_values)

        while True:
            new_freqs = {(k - 1): v for k, v in freqs.items()}
            to_reproduce = new_freqs.get(-1, None)
            if to_reproduce is not None:
                del new_freqs[-1]
                new_freqs[6] = new_freqs.get(6, 0) + to_reproduce
                new_freqs[8] = to_reproduce
            freqs = new_freqs
            yield freqs
