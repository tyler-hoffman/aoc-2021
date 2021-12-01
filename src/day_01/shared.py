from typing import List, Tuple, TypeVar


def parse(input: str) -> List[int]:
    return [int(x) for x in input.strip().split("\n")]


T = TypeVar("T")


def sliding_window(items: List[T], size: int) -> List[Tuple[T, ...]]:
    return list(zip(*[items[x : len(items) + size - 1 - x] for x in range(size)]))
