from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property
from typing import Iterator


@dataclass
class Solver(ABC):
    starts: tuple[int, int]

    @property
    @abstractmethod
    def dice(self) -> Dice:
        ...

    @cached_property
    def solution(self) -> int:
        """Generates positions of each alternating player
        until we hit >= 1000
        """
        roll_sequence = self.dice.rolls()
        alternating_players = self.alternating_players()
        while self.max_score < 1000:
            player = next(alternating_players)
            rolls = [next(roll_sequence) for _ in range(3)]
            player.position += sum(rolls)
            player.position %= 10
            player.score += player.position + 1
        loser = next(alternating_players)
        return loser.score * self.dice.roll_count

    @property
    def max_score(self) -> int:
        return max([p.score for p in self.players])

    @cached_property
    def players(self) -> tuple[Player]:
        return tuple([Player(position=p) for p in self.starts])

    def alternating_players(self) -> Iterator[Player]:
        index = 0
        while True:
            yield self.players[index]
            index = (index + 1) % 2


@dataclass
class Player(object):
    position: int
    score: int = 0


class Dice(ABC):
    roll_count = 0

    def rolls(self) -> Iterator[int]:
        while True:
            self.roll_count += 1
            yield self.next_roll()

    @abstractmethod
    def next_roll(self) -> int:
        ...
