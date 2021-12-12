from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from functools import cached_property
from typing import Iterator

from src.day_12.models import CaveSystem, Room


@dataclass
class Solver(ABC):
    @property
    @abstractmethod
    def solution(self) -> int:
        ...


@dataclass
class PathFinder(object):
    cave_system: CaveSystem
    blocked: set[Room] = field(default_factory=lambda: set([Room.start()]))
    current_path: list[Room] = field(default_factory=lambda: [Room.start()])

    @cached_property
    def end(self):
        return Room.end()

    @property
    def is_complete(self) -> bool:
        current_room = self.current_path[-1]
        return current_room == self.end

    @property
    def current_room(self) -> bool:
        return self.current_path[-1]

    def get_paths(self) -> Iterator[Room]:
        yield from self._explore()

    def _explore(self) -> Iterator[Room]:
        if self.is_complete:
            yield self.current_path.copy()
        else:
            for room in self.cave_system.connections_for_room(self.current_room):
                if not room in self.blocked:
                    if not room.is_big:
                        self.blocked.add(room)
                    self.current_path.append(room)

                    yield from self._explore()

                    self.current_path.pop()
                    if room in self.blocked:
                        self.blocked.remove(room)
