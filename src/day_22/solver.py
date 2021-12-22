from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property

from src.day_22.models import Cuboid, Instruction


@dataclass
class Solver(ABC):
    """Solver for day 22.

    The approach here is basically to maintain a list of cuboids that
    are entirely on. If we are adding a new cuboid that overlaps
    an existing one, we break up existing one, remove the intersection,
    and keep the non-intersecting sub-cuboids along with the new on one.
    For remove instructions that overlap existing on cuboids,
    we break up the existing one and remove the intersection.
    """

    instructions: list[Instruction]

    @property
    @abstractmethod
    def bounded_instructions(self) -> list[Instruction]:
        ...

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
