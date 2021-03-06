from __future__ import annotations
from dataclasses import dataclass
from functools import cached_property
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
        """Intersection of this cuboid and another

        If no intersection found returns None
        """
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

    @cached_property
    def volume(self) -> int:
        return self.x_range * self.y_range * self.z_range

    @cached_property
    def x_range(self) -> int:
        return self.max.x - self.min.x + 1

    @cached_property
    def y_range(self) -> int:
        return self.max.y - self.min.y + 1

    @cached_property
    def z_range(self) -> int:
        return self.max.z - self.min.z + 1

    @cached_property
    def is_valid(self) -> bool:
        return all(
            [
                self.max.x >= self.min.x,
                self.max.y >= self.min.y,
                self.max.z >= self.min.z,
            ]
        )

    def cuboids_after_removing(self, other: Cuboid) -> set[Cuboid]:
        """Find cuboids left after removing another

        If there is no intersection, we can return this entire cubnoid.
        If there is an intersection:
        - Assume that `other` is entirely within this cuboid
        - Split this cuboid along the edges of `other`, creating a 3x3x3
          set of sub-cuboids with the intersection at the middle
        - Filter out any invalid sub-cuboids (these occur if the `other` isn't actually
          entirely within this cuboid (i.e. if it intersects with one of the edges of
          this cuboid))
        - Filter out the intersection, since that's what we're really trying to remove here

        NOTE: We could probably be more clever and return fewer cuboids here if some could
              be merged together, but that optimization doesn't seem to be needed for a
              reasonable runtime
        """
        intersection = self.intersection(other)
        if intersection is None:
            return {self}

        x_mins = [self.min.x, intersection.min.x, intersection.max.x + 1]
        x_maxs = [intersection.min.x - 1, intersection.max.x, self.max.x]
        y_mins = [self.min.y, intersection.min.y, intersection.max.y + 1]
        y_maxs = [intersection.min.y - 1, intersection.max.y, self.max.y]
        z_mins = [self.min.z, intersection.min.z, intersection.max.z + 1]
        z_maxs = [intersection.min.z - 1, intersection.max.z, self.max.z]

        output = set[Cuboid]()
        indices = list(range(3))
        for x_index, y_index, z_index in product(indices, indices, indices):
            output.add(
                Cuboid(
                    min=Point3D(
                        x=x_mins[x_index],
                        y=y_mins[y_index],
                        z=z_mins[z_index],
                    ),
                    max=Point3D(
                        x=x_maxs[x_index],
                        y=y_maxs[y_index],
                        z=z_maxs[z_index],
                    ),
                )
            )

        return {c for c in output if c.is_valid and c != intersection}
