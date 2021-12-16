from typing import List


class Parser(object):
    @staticmethod
    def parse(input: str) -> str:
        numbers = [int(x, 16) for x in input.strip()]
        array_of_bits = [f"{x:>04b}" for x in numbers]
        all_bits = "".join(array_of_bits)
        return all_bits
