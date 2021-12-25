from __future__ import annotations

from src.day_24.models import Module


class Parser(object):
    lines_per_module = 18

    @staticmethod
    def parse(input: str) -> list[Module]:
        output = list[Module]()

        lines = input.strip().splitlines()
        module_count = len(lines) // Parser.lines_per_module

        for index in range(module_count):
            start = index * Parser.lines_per_module
            a = int(lines[start + 4].split()[2])
            b = int(lines[start + 5].split()[2])
            c = int(lines[start + 15].split()[2])
            output.append(Module(a, b, c))

        return output
