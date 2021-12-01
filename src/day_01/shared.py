from typing import List


def parse(input: str) -> List[int]:
    return [int(x) for x in input.strip().splitlines()]
