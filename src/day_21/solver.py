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
