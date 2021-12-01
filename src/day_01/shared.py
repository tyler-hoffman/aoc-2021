from typing import List, Tuple


def parse(input: str) -> List[int]:
    return [int(x) for x in input.strip().splitlines()]


def count_ascending(items: List[Tuple[int, int]]) -> int:
    return len([a for a, b in items if b > a])
