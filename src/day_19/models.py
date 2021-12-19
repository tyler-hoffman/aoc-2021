from __future__ import annotations
from dataclasses import dataclass, field
from functools import cached_property
from typing import Any


@dataclass(frozen=True)
class Point3D(object):
    x: int = 0
    y: int = 0
    z: int = 0

    def orientations(self) -> list[Point3D]:
        """Get all orientations

        Good god let this work
        """

        forward = self
        left = forward._rotate_on_z()
        back = left._rotate_on_z()
        right = back._rotate_on_z()
        up = self._rotate_on_y()
        down = up._rotate_on_y()._rotate_on_y()
        directions: list[Point3D] = [forward, left, back, right, up, down]

        output = list[Point3D]()
        for direction in directions:
            output.append(direction)
            output.append(output[-1]._rotate_on_x())
            output.append(output[-1]._rotate_on_x())
            output.append(output[-1]._rotate_on_x())

        return output

    def _rotate_on_x(self) -> Point3D:
        return Point3D(self.x, self.z, -self.y)

    def _rotate_on_y(self) -> Point3D:
        return Point3D(self.z, self.y, -self.x)

    def _rotate_on_z(self) -> Point3D:
        return Point3D(self.y, -self.x, self.z)

    def manhattan_dist(self, other: Point3D) -> int:
        x = other.x - self.x
        y = other.y - self.y
        z = other.z - self.z
        return sum([abs(value) for value in [x, y, z]])

    def __add__(self, other: Any) -> Point3D:
        if not isinstance(other, Point3D):
            raise Exception("No.")
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Any) -> Point3D:
        if not isinstance(other, Point3D):
            raise Exception("No.")
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)


@dataclass
class ScannerReading(object):
    id: int
    points: list[Point3D]
    position: Point3D = field(default_factory=Point3D)

    def shift(self, delta: Point3D) -> ScannerReading:
        points = [p + delta for p in self.points]
        return ScannerReading(id=self.id, points=points, position=self.position + delta)

    @cached_property
    def orientations(self) -> list[ScannerReading]:
        new_points_by_orientation = zip(*[p.orientations() for p in self.points])
        return [
            ScannerReading(id=self.id, points=points)
            for points in new_points_by_orientation
        ]
