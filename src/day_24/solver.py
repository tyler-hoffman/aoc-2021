from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from functools import cached_property
from typing import Iterable

from more_itertools.more import first

from src.day_24.models import Module


@dataclass
class Solver(ABC):
    modules: list[Module]
    visited: set[tuple[int, int]] = field(default_factory=set)

    @property
    def solution(self) -> int:
        winner = first(self.solve([], 0))
        return int("".join([str(x) for x in winner]))

    @abstractmethod
    def sorted_ws_to_zs(self, module: Module, z: int) -> list[dict[int, int]]:
        ...

    def solve(self, so_far: list[int], z: int) -> Iterable[list[int]]:
        index = len(so_far)
        cachable = (index, z)
        if cachable in self.visited:
            pass
        elif index == 14:
            if z == 0:
                yield so_far
        elif index < 14:
            self.visited.add(cachable)
            module = self.modules[index]
            for w, output_z in self.sorted_ws_to_zs(module, z):
                so_far.append(w)
                yield from self.solve(so_far, output_z)
                so_far.pop()
