from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from src.utils.point import Point


@dataclass
class Bounds(object):
    width: int
    height: int


@dataclass
class State(object):
    bounds: Bounds
    east_cukes: set[Point]
    south_cukes: set[Point]

    def next_state(self) -> Optional[State]:
        changed = False

        new_east_cukes = set[Point]()
        new_south_cukes = set[Point]()

        for p in self.east_cukes:
            next_east = self.next_east(p)
            if all(
                [
                    next_east not in self.east_cukes,
                    next_east not in self.south_cukes,
                ]
            ):
                new_east_cukes.add(next_east)
                changed = True
            else:
                new_east_cukes.add(p)

        for p in self.south_cukes:
            next_south = self.next_south(p)
            if all(
                [next_south not in new_east_cukes, next_south not in self.south_cukes]
            ):
                new_south_cukes.add(next_south)
                changed = True
            else:
                new_south_cukes.add(p)

        if changed:
            return State(self.bounds, new_east_cukes, new_south_cukes)
        else:
            return None

    def next_east(self, p: Point) -> Point:
        return Point(x=(p.x + 1) % self.bounds.width, y=p.y)

    def next_south(self, p: Point) -> Point:
        return Point(x=p.x, y=(p.y + 1) % self.bounds.height)
