from typing import List

from src.day_16.helpers import hex_to_binary


class Parser(object):
    @staticmethod
    def parse(input: str) -> str:
        return hex_to_binary(input.strip())
