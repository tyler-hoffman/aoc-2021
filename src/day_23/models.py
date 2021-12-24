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
    cost_so_far: int = field(default=0, compare=False)
    prev: Optional[GameState] = field(default=None, compare=False)

    def __lt__(self, other: GameState) -> bool:
        return self.optimistic_total_cost < other.optimistic_total_cost

    def __repr__(self) -> str:
        lines = []

        for y in range(7):
            chars = []
            for x in range(13):
                p = Point(x=x, y=y)
                things = [a for a in self.amphipods if a.position == p]
                if len(things) == 1:
                    chars.append(things[0].type)
                elif (
                    p in self.structure_constraints.room_points
                    or p in self.structure_constraints.hall_points
                ):
                    chars.append(" ")
                else:
                    chars.append("#")

            lines.append("".join(chars))

        lines.append(f"cost: {self.cost_so_far}")
        lines.append("")

        return "\n".join(lines)

    @cached_property
    def state_sequence(self) -> list[GameState]:
        states: list[GameState] = []
        state = self
        while state:
            states.append(state)
            state = state.prev
        return states[::-1]

    @cached_property
    def optimistic_total_cost(self) -> int:
        return self.cost_so_far + self.optimistic_remaining_cost

    @cached_property
    def optimistic_remaining_cost(self) -> int:
        return sum([self.dist_home(a) * a.move_cost for a in self.amphipods])

    @property
    def done(self) -> bool:
        return all([self.is_home(a) for a in self.amphipods])

    @property
    def num_amphipods_at_home(self):
        at_home = {self.is_home(a) for a in self.amphipods}
        return len([x for x in at_home if x])

    def dist_home(self, amphipod: Amphipod) -> int:
        hall_y = self.structure_constraints.hall_y
        if self.is_home(amphipod):
            return 0
        elif amphipod.position.y == hall_y:
            home = self.structure_constraints.first_room_for_type(amphipod.type)
            return amphipod.position.manhattan_dist(home)
        else:
            doorway = self.structure_constraints.doorway_for_type(amphipod.type)
            return 1 + amphipod.position.manhattan_dist(doorway)

    def is_home(self, amphipod: Amphipod) -> bool:
        return amphipod.position in self.structure_constraints.rooms_for_type(
            amphipod.type
        )

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
        for amphipod in self.amphipods:
            points = self.potential_moves_for_amphipod(amphipod)
            for pos in points:
                output.add(self.move_amphipod(amphipod, pos))
        return output

    @cache
    def potential_moves_for_amphipod(self, amphipod: Amphipod) -> set[Point]:
        hall_y = self.structure_constraints.hall_y
        has_wrong_type_in_amphipods_room = self.has_wrong_amphipod_in_room(
            amphipod.type
        )

        if amphipod.moves_so_far >= 2:
            targets = []
        elif amphipod.position.y == hall_y and not has_wrong_type_in_amphipods_room:
            # need to go home
            target = self.lowest_unoccupied_room_for_type(amphipod.type)
            targets = [target] if target else []
        elif self.is_home(amphipod) and not has_wrong_type_in_amphipods_room:
            target = self.lowest_unoccupied_room_for_type(amphipod.type)
            if target and target.y > amphipod.position.y:
                return [target]
            else:
                return []
        elif self.is_home(amphipod) and amphipod.moves_so_far == 0:
            targets = self.structure_constraints.rooms_for_type(amphipod.type)
            targets = [t for t in targets if t.y > amphipod.position.y] + list(
                self.structure_constraints.valid_hall_positions
            )
        elif self.is_home(amphipod) and amphipod.moves_so_far == 1:
            targets = self.structure_constraints.rooms_for_type(amphipod.type)
            targets = [t for t in targets if t.y > amphipod.position.y]
        elif amphipod.moves_so_far == 0:
            # move out of room
            targets = self.structure_constraints.valid_hall_positions
        else:
            targets = []

        output = set[Point]()
        for target in targets:
            if self.can_get_to(amphipod, target):
                output.add(target)
        return output

    @cache
    def lowest_unoccupied_room_for_type(self, type: str) -> Optional[Point]:
        rooms = self.structure_constraints.rooms_for_type(type)
        unoccupied_rooms = [r for r in rooms if r not in self.occupied_points]

        if len(unoccupied_rooms) > 0:
            return unoccupied_rooms[-1]
        else:
            return None

    def can_get_to(self, amphipod: Amphipod, pos: Point) -> bool:
        hall_y = self.structure_constraints.hall_y
        if amphipod.position.y == hall_y and pos.y != hall_y:
            # Go home
            doorway = self.structure_constraints.doorway_for_type(amphipod.type)
            return self.can_move_horizontally_to(
                amphipod.position, doorway
            ) and self.can_move_vertically_to(doorway, pos)
        elif amphipod.position.y != hall_y and pos.y == hall_y:
            # Leave room
            doorway = Point(x=amphipod.position.x, y=hall_y)
            # doorway = self.structure_constraints.doorway_for_type(amphipod.type)
            return self.can_move_vertically_to(
                amphipod.position, doorway
            ) and self.can_move_horizontally_to(doorway, pos)
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
        cost_to_move = amphipod.cost_to_move_to(pos)
        new_amphipod = amphipod.move_to(pos)
        new_amphipods = self.amphipods.difference({amphipod}).union({new_amphipod})
        new_cost = self.cost_so_far + cost_to_move

        return GameState(
            structure_constraints=self.structure_constraints,
            amphipods=new_amphipods,
            cost_so_far=new_cost,
            prev=self,
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
        return Amphipod(
            type=self.type,
            position=pos,
            moves_so_far=self.moves_so_far + 1,
        )

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
