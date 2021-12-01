from typing import List, Tuple, TypeVar

T = TypeVar("T")


def sliding_window(items: List[T], size: int) -> List[Tuple[T, ...]]:
    zip_parts: List[List[T]] = []
    end_offset = len(items) + size - 1

    for offset in range(size):
        zip_parts.append(items[offset : end_offset - offset])

    for window in zip(*zip_parts):
        yield window
