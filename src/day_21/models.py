from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Player(object):
    position: int
    score: int = 0

    def move(self, amt: int) -> Player:
        self.position += amt
        self.position %= 10
        self.score += self.position + 1


@dataclass(frozen=True)
class PlayerState(object):
    position: int
    score: int = 0

    def move(self, amt: int) -> PlayerState:
        position = (self.position + amt) % 10
        score = self.score + position + 1
        return PlayerState(position=position, score=score)

@dataclass(frozen=True)
class GameState(object):
    player_a: PlayerState
    player_b: PlayerState
    score_to_win: int
    is_player_a_turn: bool = True

    def move(self, amt: int) -> GameState:
        if self.is_player_a_turn:
            return GameState(
                player_a=self.player_a.move(amt),
                player_b=self.player_b,
                score_to_win=self.score_to_win,
                is_player_a_turn=False,
            )
        else:
            return GameState(
                player_a=self.player_a,
                player_b=self.player_b.move(amt),
                score_to_win=self.score_to_win,
                is_player_a_turn=True,
            )

    @property
    def won(self) -> bool:
        return self.player_a_won or self.player_b_won

    @property
    def player_a_won(self) -> bool:
        return self.player_a.score >= self.score_to_win

    @property
    def player_b_won(self) -> bool:
        return self.player_b.score >= self.score_to_win