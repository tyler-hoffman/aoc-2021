from functools import cache
from typing import List

from src.day_23.models import AMPHIPOD_TYPES, Amphipod, GameState, StructureConstraints
from src.utils.point import Point

EXTRA_LINES = """
GARBAGE_PLACEHOLDER_LINE
  #D#C#B#A#
  #D#B#A#C#
"""

class Parser(object):
    @staticmethod
    def parse(input: str) -> GameState:
        lines = input.strip().splitlines()

        return Parser.parse_lines(lines)

    @staticmethod
    def parse_with_folds(input: str) -> GameState:
        lines = input.strip().splitlines()
        middle_lines = EXTRA_LINES.strip().splitlines()
        lines = lines[:-2] + middle_lines[1:] + lines[-2:]

        amphipods = Parser.parse_amphipods(lines)
        hall_points = Parser.parse_hall_positions(lines[1], 1)
        room_points = frozenset([a.position for a in amphipods])

        structure_constraints = StructureConstraints(
            hall_points=hall_points, room_points=room_points
        )
        return GameState(
            structure_constraints=structure_constraints, amphipods=amphipods
        )

    @staticmethod
    def parse_lines(lines: list[str]) -> GameState:
        amphipods = Parser.parse_amphipods(lines)
        hall_points = Parser.parse_hall_positions(lines[1], 1)
        room_points = frozenset([a.position for a in amphipods])

        structure_constraints = StructureConstraints(
            hall_points=hall_points, room_points=room_points
        )
        return GameState(
            structure_constraints=structure_constraints, amphipods=amphipods
        )

    @staticmethod
    def parse_hall_positions(line: str, y: int) -> frozenset[Point]:
        return frozenset({Point(x=x, y=y) for x, ch in enumerate(line) if ch == "."})

    @staticmethod
    def parse_amphipods(lines: list[str]) -> frozenset[Amphipod]:
        amphipods = list[Amphipod]()
        for y, line in enumerate(lines):
            for x, ch in enumerate(line):
                if ch in AMPHIPOD_TYPES:
                    amphipods.append(Amphipod(type=ch, position=Point(x=x, y=y)))
        return frozenset(amphipods)
