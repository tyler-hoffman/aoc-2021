from typing import List


def parse(input: str) -> List[str]:
    return input.strip().splitlines()


def array_to_int(bits: List[str]) -> int:
    as_str = "".join(bits)
    return int(as_str, 2)
