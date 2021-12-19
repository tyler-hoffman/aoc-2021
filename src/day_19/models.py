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
        left = forward.rotate_on_z()
        back = left.rotate_on_z()
        right = back.rotate_on_z()
        up = self.rotate_on_y()
        down = up.rotate_on_y().rotate_on_y()
        directions: list[Point3D] = [forward, left, back, right, up, down]

        output = list[Point3D]()
        for direction in directions:
            output.append(direction)
            output.append(output[-1].rotate_on_x())
            output.append(output[-1].rotate_on_x())
            output.append(output[-1].rotate_on_x())

        return output

    def rotate_on_x(self) -> Point3D:
        return Point3D(self.x, self.z, -self.y)

    def rotate_on_y(self) -> Point3D:
        return Point3D(self.z, self.y, -self.x)

    def rotate_on_z(self) -> Point3D:
        return Point3D(self.y, -self.x, self.z)

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
        return ScannerReading(id=self.id, points=points) 

    @cached_property
    def orientations(self) -> list[ScannerReading]:
        new_points_by_orientation = zip(*[p.orientations() for p in self.points])
        return [ScannerReading(id=self.id, points=points) for points in new_points_by_orientation]

    @cached_property
    def max_x(self) -> int:
        return max([p.x for p in self.points])

    @cached_property
    def min_x(self) -> int:
        return min([p.x for p in self.points])

    @cached_property
    def max_y(self) -> int:
        return max([p.y for p in self.points])

    @cached_property
    def min_y(self) -> int:
        return min([p.y for p in self.points])

    @cached_property
    def max_z(self) -> int:
        return max([p.z for p in self.points])

    @cached_property
    def min_z(self) -> int:
        return min([p.z for p in self.points])
