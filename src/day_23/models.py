from __future__ import annotations
from dataclasses import dataclass, field
from functools import cache, cached_property, total_ordering
from typing import Optional
from src.utils.point import Point


AMPHIPOD_TYPES: frozenset[str] = frozenset(["A", "B", "C", "D"])


@total_ordering
@dataclass(frozen=True)
class GameState(object):
    structure_constraints: StructureConstraints
    amphipods: frozenset[Amphipod]
    cost: int = field(default=0)

    def __lt__(self, other: GameState) -> bool:
        if self.cost < other.cost:
            return True
        elif self.cost > other.cost:
            return False
        else:
            return self.num_amphipods_at_home > other.num_amphipods_at_home


    @property
    def done(self) -> bool:
        return all([self.is_home(a) for a in self.amphipods])

    @property
    def num_amphipods_at_home(self):
        at_home = {self.is_home(a) for a in self.amphipods}
        return len([x for x in at_home if x])

    def is_home(self, amphipod: Amphipod) -> bool:
        return amphipod.position in self.structure_constraints.rooms_for_type(amphipod.type)

    @cached_property
    def occupied_points(self) -> dict[Point, Amphipod]:
        return {a.position: a for a in self.amphipods}

    def has_wrong_amphipod_in_room(self, room_type: str) -> bool:
        amphipods = self.amphipods_in_room(room_type)
        return any([a.type != room_type for a in amphipods])

    def amphipods_in_room(self, room_type: str) -> set[Amphipod]:
        output = set[Amphipod]()
        room_points = self.structure_constraints.rooms_for_type(room_type)
        for point in room_points:
            if amphipod := self.occupied_points.get(point):
                output.add(amphipod)
        return output

    def potential_new_states(self) -> set[GameState]:
        output = set[GameState]()
        amphids_with_remaining_moves = [a for a in self.amphipods if a.moves_so_far < 2]
        for amphipod in amphids_with_remaining_moves:
            points = self.potential_moves_for_amphipod(amphipod)
            for pos in points:
                output.add(self.move_amphipod(amphipod, pos))
        return output

    def potential_moves_for_amphipod(self, amphipod: Amphipod) -> set[Point]:
        hall_y = self.structure_constraints.hall_y
        output = set[Point]()
        if amphipod.position.y == hall_y:
            # need to go home
            targets = self.structure_constraints.rooms_for_type(amphipod.type)
        elif self.is_home(amphipod) and not self.has_wrong_amphipod_in_room(amphipod.type):
            # maybe scoot down
            targets = self.structure_constraints.rooms_for_type(amphipod.type)
            targets = [t for t in targets if t.y > amphipod.position.y]
        elif self.is_home(amphipod):
            targets = self.structure_constraints.rooms_for_type(amphipod.type)
            targets = [t for t in targets if t.y > amphipod.position.y] + list(self.structure_constraints.valid_hall_positions)
        else:
            # move out of room
            targets = self.structure_constraints.valid_hall_positions

        for target in targets:
            if self.can_get_to(amphipod, target):
                output.add(target)
        return output

    def can_get_to(self, amphipod: Amphipod, pos: Point) -> bool:
        hall_y = self.structure_constraints.hall_y
        if amphipod.position.y == hall_y and pos.y != hall_y:
            # Go home
            doorway = self.structure_constraints.doorway_for_type(amphipod.type)
            return self.can_move_horizontally_to(amphipod.position, doorway) and self.can_move_vertically_to(doorway, pos)
        elif amphipod.position.y != hall_y and pos.y == hall_y:
            # Leave home
            doorway = self.structure_constraints.doorway_for_type(amphipod.type)
            return self.can_move_vertically_to(amphipod.position, doorway) and self.can_move_horizontally_to(doorway, pos)
        elif amphipod.position.x == pos.x:
            # move rooms
            return self.can_move_vertically_to(amphipod.position, pos)
        else:
            raise Exception("You shouldn't be trying to move just horizontally")

    def can_move_horizontally_to(self, point: Point, dest: Point) -> bool:
        while point.x > dest.x:
            point += Point(x=-1, y=0)
            if point in self.occupied_points:
                return False
        while point.x < dest.x:
            point += Point(x=1, y=0)
            if point in self.occupied_points:
                return False
        return True

    def can_move_vertically_to(self, point: Point, dest: Point) -> bool:
        while point.y > dest.y:
            point += Point(x=0, y=-1)
            if point in self.occupied_points:
                return False
        while point.y < dest.y:
            point += Point(x=0, y=1)
            if point in self.occupied_points:
                return False
        return True

    def move_amphipod(self, amphipod: Amphipod, pos: Point) -> GameState:
        new_amphipod = amphipod.move_to(pos)
        new_amphipods = self.amphipods.difference({amphipod}).union({new_amphipod})
        new_cost = self.cost + amphipod.cost_to_move_to(pos)

        return GameState(
            structure_constraints=self.structure_constraints,
            amphipods=new_amphipods,
            cost=new_cost,
        )


@dataclass(frozen=True)
class StructureConstraints(object):
    hall_points: frozenset[Point]
    room_points: frozenset[Point]

    @cached_property
    def valid_hall_positions(self) -> set[Point]:
        return self.hall_points - self.doorways

    @cached_property
    def doorways(self) -> set[Point]:
        return set([self.doorway_for_type(x) for x in AMPHIPOD_TYPES])

    @cache
    def doorway_for_type(self, type: str) -> Point:
        return Point(x=self.first_room_for_type(type).x, y=self.hall_y)

    @cache
    def first_room_for_type(self, type: str) -> Point:
        return self.rooms_for_type(type)[0]

    @cache
    def rooms_for_type(self, type: str) -> tuple[Point, ...]:
        return self.rooms_by_type[type]

    @cached_property
    def room_ys(self) -> list[int]:
        return sorted({p.y for p in self.room_points})

    @cached_property
    def hall_y(self) -> list[int]:
        return list(self.hall_points)[0].y

    @cached_property
    def rooms_by_type(self) -> dict[str, tuple[Point, ...]]:
        xs = sorted({p.x for p in self.room_points})
        ys = sorted({p.y for p in self.room_points})
        ax, bx, cx, dx = xs
        return {
            "A": tuple([Point(x=ax, y=y) for y in ys]),
            "B": tuple([Point(x=bx, y=y) for y in ys]),
            "C": tuple([Point(x=cx, y=y) for y in ys]),
            "D": tuple([Point(x=dx, y=y) for y in ys]),
        }


@dataclass(frozen=True)
class Amphipod(object):
    type: str
    position: Point
    moves_so_far: int = 0

    def move_to(self, pos: Point) -> Amphipod:
        return Amphipod(type=self.type, position=self.position + pos, moves_so_far=self.moves_so_far+1)

    def cost_to_move_to(self, p: Point) -> int:
        return self.move_cost * self.position.manhattan_dist(p)

    @property
    def move_cost(self) -> int:
        return self.move_cost_by_type[self.type]

    @classmethod
    @property
    @cache
    def move_cost_by_type(self) -> dict[str, int]:
        return {
            "A": 1,
            "B": 10,
            "C": 100,
            "D": 1000,
        }
