from dataclasses import dataclass
from typing import List


@dataclass
class Entry:
    signal_patterns: List[str]
    output_value: List[str]
