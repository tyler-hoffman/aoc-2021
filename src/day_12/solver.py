from __future__ import annotations
from dataclasses import dataclass, field
from functools import cache
from typing import Iterator

from src.day_12.models import CaveSystem, Room


@dataclass
class Solver(object):
    path_finder: PathFinder

    @property
    def solution(self) -> int:
        count = 0
        paths = []
        for path in self.path_finder.get_paths():
            count += 1
            paths.append(path)
        return count


@dataclass
class PathFinder(object):
    cave_system: CaveSystem
    current_path: list[Room] = field(default_factory=lambda: [PathFinder.start])
    room_visit_count: dict[Room, int] = field(
        default_factory=lambda: {PathFinder.start: 1}
    )

    @classmethod
    @property
    @cache
    def start(cls) -> Room:
        return Room("start")

    @classmethod
    @property
    @cache
    def end(cls) -> Room:
        return Room("end")

    @property
    def is_complete(self) -> bool:
        return self.current_room == self.end

    @property
    def current_room(self) -> bool:
        return self.current_path[-1]

    def get_visit_count(self, room: Room) -> int:
        return self.room_visit_count.get(room, 0)

    def change_visit_count(self, room: Room, amt: int) -> None:
        self.room_visit_count[room] = self.get_visit_count(room) + amt

    def can_explore_room(self, room: Room) -> bool:
        return room.is_big or not self.get_visit_count(room)

    def get_paths(self) -> Iterator[Room]:
        yield from self._explore()

    def _explore_room(self, room: Room) -> Iterator[Room]:
        self.change_visit_count(room, 1)
        self.current_path.append(room)

        yield from self._explore()

        self.current_path.pop()
        self.change_visit_count(room, -1)

    def _explore(self) -> Iterator[Room]:
        if self.is_complete:
            yield self.current_path.copy()
        else:
            for room in self.cave_system.room_connections(self.current_room):
                if self.can_explore_room(room):
                    yield from self._explore_room(room)
