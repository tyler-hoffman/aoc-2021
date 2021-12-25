from dataclasses import dataclass, field
from functools import cache
from more_itertools import first
from typing import Callable, Iterable
from src.day_24.models import Module, Operator
from src.day_24.parser import Parser
from src.day_24.solver import Solver


@dataclass
class Day24PartASolver(Solver):
    modules: list[Module]
    visited: set[tuple[int, int]] = field(default_factory=set)

    @property
    def solution(self) -> int:
        winner = first(self.solve([], 0))
        return int("".join([str(x) for x in winner]))


    def solve(self, so_far: list[int], z: int) -> Iterable[list[int]]:
        index = len(so_far)
        cachable = (index, z)
        if cachable in self.visited:
            pass
        elif index == 14:
            if z  == 0:
                yield so_far
        elif index < 14:
            self.visited.add(cachable)
            module = self.modules[index]
            ws_to_output_zs = module.ws_to_output_zs(z)
            for w, output_z in sorted(ws_to_output_zs.items(), reverse=True):
                so_far.append(w)
                yield from self.solve(so_far, output_z)
                so_far.pop()





def solve(input: str) -> int:
    modules = Parser.parse(input)
    solver = Day24PartASolver(modules)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_24/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
