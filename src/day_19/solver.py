from abc import ABC
from dataclasses import dataclass, field
from functools import cached_property
from itertools import product
from typing import Optional

from src.day_19.models import ScannerReading
from src.utils.collections import frequency_map


NEEDED_FOR_MATCH = 12


@dataclass
class Solver(ABC):
    scanner_readings: list[ScannerReading]
    checked: set[tuple[int, int]] = field(default_factory=set)

    @cached_property
    def oriented_scanners(self) -> None:
        grouped = [self.scanner_readings[0]]
        remaining = self.scanner_readings[1:]

        doing_it = True
        while doing_it:
            doing_it = False

            for reading in remaining.copy():
                to_add = self.find_valid_orientation_if_possible(grouped, reading)
                if to_add is not None:
                    doing_it = True
                    remaining = [r for r in remaining if r.id != reading.id]
                    grouped.append(to_add)

        assert not len(remaining)
        assert len(grouped) == len(self.scanner_readings)
        return grouped

    def find_valid_orientation_if_possible(
        self, grouped: list[ScannerReading], reading: ScannerReading
    ) -> Optional[ScannerReading]:
        for base in grouped:
            pair_id = (base.id, reading.id)
            if pair_id not in self.checked:
                self.checked.add(pair_id)
                match = self.find_offset_for_match(base, reading)
                if match is not None:
                    return match
        return None

    def find_offset_for_match(
        self, base: ScannerReading, to_check: ScannerReading
    ) -> Optional[ScannerReading]:
        for orientation in to_check.orientations:
            diffs = [a - b for a, b in product(base.points, orientation.points)]
            diffs_by_freq = frequency_map(diffs)
            filtered = [
                point
                for point, count in diffs_by_freq.items()
                if count >= NEEDED_FOR_MATCH
            ]

            assert len(filtered) < 2
            if len(filtered) == 1:
                delta = filtered[0]
                return orientation.shift(delta)
        return None
