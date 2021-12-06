from typing import List


class Parser(object):
    def parse(self, input: str) -> List[str]:
        return [int(x) for x in input.split(",")]
