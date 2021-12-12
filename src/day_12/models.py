from __future__ import annotations
from dataclasses import dataclass
from functools import cache, cached_property


@dataclass(frozen=True)
class Room(object):
    name: str

    @cached_property
    def is_big(self) -> bool:
        return self.name.isupper()

    @cached_property
    def is_small(self) -> bool:
        return not self.is_big


@dataclass
class CaveSystem(object):
    explicit_connections: set[tuple[Room, Room]]

    def room_connections(self, room: Room) -> set[Room]:
        return self.connections_by_rooom[room]

    @cached_property
    def connections_by_rooom(self) -> dict[Room, set[Room]]:
        output = {room: set() for room in self.rooms}
        for a, b in self.explicit_connections:
            output[a].add(b)
            output[b].add(a)
        return output

    @cached_property
    def rooms(self) -> set[Room]:
        output = set[Room]()
        for k, v in self.explicit_connections:
            output.add(k)
            output.add(v)
        return output
