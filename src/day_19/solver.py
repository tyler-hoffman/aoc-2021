from abc import ABC
from dataclasses import dataclass, field
from itertools import product
from typing import Optional

from src.day_19.models import Point3D, ScannerReading
from src.utils.collections import frequency_map


NEEDED_FOR_MATCH = 12

@dataclass
class Solver(ABC):
    scanner_readings: list[ScannerReading]
    checked: set[tuple[int, int]] = field(default_factory=set)
    grouped: list[ScannerReading] = field(default_factory=list)
    remaining: list[ScannerReading] = field(default_factory=list)

    def group_them(self) -> None:
        self.grouped = [self.scanner_readings[0]]
        self.remaining = self.scanner_readings[1:]

        doing_it = True
        while doing_it:
            doing_it = False

            for reading in self.remaining.copy():
                doing_it = doing_it or self.attempt_to_add(reading)

        assert not len(self.remaining)

    def attempt_to_add(self, reading: ScannerReading) -> bool:
        for base in self.grouped:
            pair_id = (base.id, reading.id)
            if pair_id not in self.checked:
                self.checked.add(pair_id)
                match = self.find_offset_for_match(base, reading)
                if match is not None:
                    self.remaining = [r for r in self.remaining if r.id != reading.id]
                    self.grouped.append(match)
                    return True
        return False

    def find_offset_for_match(self, base: ScannerReading, to_check: ScannerReading) -> Optional[ScannerReading]:
        for orientation in to_check.orientations:
            diffs = [a - b for a, b in product(base.points, orientation.points)]
            # diffs = [p for p in diffs if all([
            #     abs(orientation.max_x - p.x) <= 1000,
            #     abs(orientation.max_y - p.y) <= 1000,
            #     abs(orientation.max_z - p.z) <= 1000,
            #     abs(orientation.min_x - p.x) <= 1000,
            #     abs(orientation.min_y - p.y) <= 1000,
            #     abs(orientation.min_z - p.z) <= 1000,
            # ])]
            diffs_by_freq = frequency_map(diffs)
            filtered = [point for point, count in diffs_by_freq.items() if count >= NEEDED_FOR_MATCH]

            assert len(filtered) < 2
            if len(filtered) == 1:
                delta = filtered[0]
                return orientation.shift(delta)
        return None
