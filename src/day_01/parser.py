from typing import List


class Parser(object):
    def parse(self, input: str) -> List[int]:
        return [int(x) for x in input.strip().splitlines()]
