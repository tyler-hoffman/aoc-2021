from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property
from typing import Iterator

from src.day_21.models import GameState, PlayerState


@dataclass
class Solver(ABC):
    starts: tuple[int, int]

    @property
    @abstractmethod
    def score_to_win(self) -> int:
        ...

    @cached_property
    def starting_state(self) -> GameState:
        return GameState(
            player_a=PlayerState(position=self.starts[0]),
            player_b=PlayerState(position=self.starts[1]),
            score_to_win=self.score_to_win,
        )

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
