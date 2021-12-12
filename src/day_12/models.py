from __future__ import annotations
from dataclasses import dataclass
from functools import cache, cached_property


@dataclass(frozen=True)
class Room(object):
    name: str

    @cached_property
    def is_big(self) -> bool:
        return self.name.isupper()

    @staticmethod
    def start() -> Room:
        return Room("start")

    @staticmethod
    def end() -> Room:
        return Room("end")


@dataclass
class CaveSystem(object):
    explicit_connections: set[tuple[Room, Room]]

    def connections_for_room(self, room: Room) -> set[Room]:
        return self.connections_from_rooms[room]

    @cached_property
    def connections_from_rooms(self) -> dict[Room, set[Room]]:
        output = {room: set() for room in self.rooms}
        for a, b in self.connections:
            output[a].add(b)
        return output

    @cached_property
    def connections(self) -> set[tuple[Room, Room]]:
        output = set[tuple[Room, Room]]()
        for start, end in self.explicit_connections:
            output.add((start, end))
            output.add((end, start))
        return output

    @cached_property
    def rooms(self) -> set[Room]:
        output = set[Room]()
        for k, v in self.explicit_connections:
            output.add(k)
            output.add(v)
        return output
