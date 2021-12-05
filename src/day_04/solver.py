from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterator, List, Set

from src.day_04.board import Board


@dataclass
class WinningState(object):
    board: Board
    draws: Set[int]
    last_draw: int

    @property
    def score(self) -> int:
        unmarked = self.board.unmarked_stuff(self.draws)
        return sum(unmarked) * self.last_draw


@dataclass
class Solver(ABC):
    boards: List[Board]
    draws: List[int]

    @property
    @abstractmethod
    def solution(self) -> int:
        ...

    @property
    def _winning_states(self) -> Iterator[WinningState]:
        drawn: Set[int] = set()
        remaining_boards = self.boards.copy()

        for item in self.draws:
            drawn.add(item)

            for board in remaining_boards:
                if board.wins(drawn):
                    remaining_boards.remove(board)
                    yield WinningState(board=board, draws=drawn.copy(), last_draw=item)
