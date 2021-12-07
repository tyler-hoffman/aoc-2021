from typing import List


class Parser(object):
    @staticmethod
    def parse(input: str) -> List[str]:
        return input.strip().splitlines()
