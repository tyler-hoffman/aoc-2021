from dataclasses import dataclass
from typing import List


Chunk = frozenset[str]


@dataclass
class Entry:
    signal_patterns: List[Chunk]
    output_value: List[Chunk]
