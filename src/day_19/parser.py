from typing import List

from src.day_19.models import Point3D, ScannerReading


class Parser(object):
    @staticmethod
    def parse(input: str) -> List[ScannerReading]:
        output = list[ScannerReading]()
        points = list[Point3D]()

        for line in input.strip().splitlines():
            if not line:
                continue
            elif "scanner" in line:
                if points:
                    output.append(ScannerReading(id=len(output), points=points))
                points = []
            else:
                points.append(Parser.parse_point(line))

        output.append(ScannerReading(id=len(output), points=points))
        return output

    @staticmethod
    def parse_point(line: str) -> Point3D:
        x, y, z = [int(x) for x in line.split(",")]
        return Point3D(x, y, z)