from typing import Iterator, List, Tuple


def parse(input: str) -> List[int]:
    return [int(x) for x in input.strip().splitlines()]


def count_ascending(items: Iterator[Tuple[int, int]]) -> int:
    return len([a for a, b in items if b > a])
