from typing import List

from src.day_08.models import Entry


class Parser(object):
    @staticmethod
    def parse_line(line: str) -> Entry:
        first_part, second_part = line.split(" | ")
        signal_paterns = [frozenset(x) for x in first_part.split()]
        output_value = [frozenset(x) for x in second_part.split()]

        return Entry(signal_patterns=signal_paterns, output_value=output_value)

    @staticmethod
    def parse(input: str) -> List[Entry]:
        return [Parser.parse_line(line) for line in input.strip().splitlines()]
