from typing import List

from src.day_11.models import OctopusCluster
from src.utils.point import Point


class Parser(object):
    @staticmethod
    def parse(input: str) -> OctopusCluster:
        output: OctopusCluster = {}

        for y, line in enumerate(input.strip().splitlines()):
            for x, value in enumerate(line):
                output[Point(x=x, y=y)] = int(value)

        return output
