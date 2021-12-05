import dataclasses
import re
from typing import List

from src.day_04.board import Board


@dataclasses.dataclass
class Data(object):
    boards: List[Board]
    draws: List[int]


class Parser(object):
    def parse(self, input: str) -> Data:
        lines = input.strip().splitlines()

        draws = [int(x) for x in lines[0].split(",")]
        boards: List[Board] = []

        for index in range(2, len(lines), 6):
            board_data: List[List[int]] = []
            for line in lines[index : index + 5]:
                board_data.append([int(x) for x in re.split("\s+", line.strip())])
            boards.append(Board(lines=board_data))

        return Data(boards=boards, draws=draws)
