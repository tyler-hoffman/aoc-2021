from typing import List

from src.day_14.models import Data, Rule


class Parser(object):
    @classmethod
    def parse(cls, input: str) -> Data:
        lines = input.strip().splitlines()
        template = lines[0]
        rules = {cls.parse_rule(line) for line in lines[2:]}

        return Data(template=template, rules=rules)

    @classmethod
    def parse_rule(cls, line: str) -> Rule:
        ab, production = line.split(" -> ")
        a, b = ab
        return Rule(left=a, right=b, produces=production)
