from typing import List

from src.day_12.models import CaveSystem, Room


class Parser(object):
    @staticmethod
    def parse(input: str) -> CaveSystem:
        connections = {
            Parser.parse_connection(line) for line in input.strip().splitlines()
        }
        return CaveSystem(explicit_connections=connections)

    @staticmethod
    def parse_connection(line: str) -> tuple[Room, Room]:
        a, b = line.split("-")
        return Room(a), Room(b)
