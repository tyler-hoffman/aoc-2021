from dataclasses import dataclass
from typing import Iterator
from src.day_12.models import Room
from src.day_12.parser import Parser
from src.day_12.solver import PathFinder, Solver


def solve(input: str) -> int:
    cave_system = Parser.parse(input)
    path_finder = PathFinderB(cave_system=cave_system)
    solver = Solver(path_finder=path_finder)

    return solver.solution


@dataclass
class PathFinderB(PathFinder):
    double_checked_a_small_room: bool = False

    def can_explore_room(self, room: Room) -> bool:
        visit_count = self.get_visit_count(room)
        if room.is_big or visit_count == 0:
            return True
        elif room == self.start:
            return False
        else:
            return not self.double_checked_a_small_room

    def _explore_room(self, room: Room) -> Iterator[Room]:
        use_double_check = room.is_small and self.get_visit_count(room) > 0

        if use_double_check:
            self.double_checked_a_small_room = True

        yield from super()._explore_room(room)

        if use_double_check:
            self.double_checked_a_small_room = False


if __name__ == "__main__":
    with open("src/day_12/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
