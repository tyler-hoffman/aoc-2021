import re
from src.day_17.models import TargetArea


class Parser(object):
    @staticmethod
    def parse(input: str) -> TargetArea:
        numbers = re.findall(r"-?\d+", input)
        x_min, x_max, y_min, y_max = [int(number) for number in numbers]

        return TargetArea(x_min=x_min, x_max=x_max, y_min=y_min,y_max=y_max)
