from dataclasses import dataclass
from functools import cached_property
import re
from typing import List

from src.day_18.solver import SnailfishLeafNode, SnailfishNumber, SnailfishPair


@dataclass
class Parser(object):
    line: str
    depth: int = 0
    index: int = 0

    def get_snailfish_number(self) -> SnailfishNumber:
        self.depth = 0
        self.index = 0

        return self.parse_node()

    def parse_node(self) -> SnailfishNumber:
        match self.current_token:
            case "[":
                return self.parse_pair()
            case _:
                return self.parse_number()

    def parse_pair(self) -> SnailfishPair:
        self.throw_away_current("[")
        left = self.parse_node()
        right = self.parse_node()
        self.throw_away_current("]")

        pair = SnailfishPair(left=left, right=right, parent=None)
        left.parent = pair
        right.parent = pair

        return pair

    def parse_number(self) -> SnailfishPair:
        assert isinstance(self.current_token, int)
        number = SnailfishLeafNode(value=self.current_token, parent=None)
        self.increment()
        return number

    def throw_away_current(self, token: str) -> None:
        assert self.current_token == token
        self.increment()

    @property
    def current_token(self) -> str:
        return self.tokens[self.index]

    def increment(self) -> None:
        self.index += 1

    @cached_property
    def tokens(self) -> list[str]:
        strings = re.findall(r"(\[|\]|\d+)", self.line)
        return [s if s in ("[", "]") else int(s) for s in strings]

    @staticmethod
    def parse(input: str) -> List[SnailfishNumber]:
        lines = input.strip().splitlines()
        return [Parser(line).get_snailfish_number() for line in lines if line]
