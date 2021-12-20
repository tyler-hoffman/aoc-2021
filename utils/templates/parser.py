PARSER_TEMPLATE = """
from typing import List


class Parser(object):
    @staticmethod
    def parse(input: str) -> List[str]:
        raise NotImplementedError()

"""
