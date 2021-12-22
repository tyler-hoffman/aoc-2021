from __future__ import annotations
from dataclasses import dataclass
from itertools import product
from typing import Iterator


@dataclass
class Instruction(object):
    cuboid: Cuboid
    on: bool


@dataclass(frozen=True)
class Point3D(object):
    x: int
    y: int
    z: int


@dataclass
class Cuboid(object):
    min: Point3D
    max: Point3D

    def all_contained_points(self) -> Iterator[Point3D]:
        output = set[Point3D]()

        xs = range(self.min.x, self.max.x + 1)
        ys = range(self.min.y, self.max.y + 1)
        zs = range(self.min.z, self.max.z + 1)

        for x, y, z in product(xs, ys, zs):
            yield Point3D(x=x, y=y, z=z)

        return output

    def is_valid(self) -> bool:
        return all(
            [
                self.max.x >= self.min.x,
                self.max.y >= self.min.y,
                self.max.z >= self.min.z,
            ]
        )
