from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property

from src.day_22.models import Cuboid, Instruction


@dataclass
class Solver(ABC):
    instructions: list[Instruction]

    @property
    def solution(self) -> int:
        return sum([c.volume for c in self.all_on_cuboids])

    @cached_property
    def all_on_cuboids(self) -> set[Cuboid]:
        non_overlapping_cuboids = set[Cuboid]()

        for instruction in self.bounded_instructions:
            new_non_overlapping_cuboids = set[Cuboid]()
            cuboid = instruction.cuboid
            if instruction.on:
                for other in non_overlapping_cuboids:
                    new_non_overlapping_cuboids.update(
                        other.cuboids_after_removing(cuboid)
                    )
                new_non_overlapping_cuboids.add(cuboid)
            else:
                for other in non_overlapping_cuboids:
                    new_non_overlapping_cuboids.update(
                        other.cuboids_after_removing(cuboid)
                    )
            non_overlapping_cuboids = new_non_overlapping_cuboids

        return non_overlapping_cuboids

    @property
    @abstractmethod
    def bounded_instructions(self) -> list[Instruction]:
        ...
