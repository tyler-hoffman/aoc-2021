from __future__ import annotations
from dataclasses import dataclass
from itertools import product
from typing import Iterator, Optional


@dataclass
class Instruction(object):
    cuboid: Cuboid
    on: bool


@dataclass(frozen=True)
class Point3D(object):
    x: int
    y: int
    z: int


@dataclass(frozen=True)
class Cuboid(object):
    min: Point3D
    max: Point3D

    def all_contained_points(self) -> Iterator[Point3D]:
        xs = range(self.min.x, self.max.x + 1)
        ys = range(self.min.y, self.max.y + 1)
        zs = range(self.min.z, self.max.z + 1)

        for x, y, z in product(xs, ys, zs):
            yield Point3D(x=x, y=y, z=z)

    def intersection(self, other: Cuboid) -> Optional[Cuboid]:
        if self.has_intersection(other):
            return Cuboid(
                min=Point3D(
                    x=max(self.min.x, other.min.x),
                    y=max(self.min.y, other.min.y),
                    z=max(self.min.z, other.min.z),
                ),
                max=Point3D(
                    x=min(self.max.x, other.max.x),
                    y=min(self.max.y, other.max.y),
                    z=min(self.max.z, other.max.z),
                ),
            )
        else:
            return None

    def has_intersection(self, other: Cuboid) -> bool:
        return all(
            [
                other.min.x <= self.max.x,
                other.min.y <= self.max.y,
                other.min.z <= self.max.z,
                other.max.x >= self.min.x,
                other.max.y >= self.min.y,
                other.max.z >= self.min.z,
            ]
        )
