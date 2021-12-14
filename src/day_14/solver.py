from dataclasses import dataclass
from functools import cached_property
from more_itertools import sliding_window

from src.utils.collections import frequency_map
from src.day_14.models import Pair, Rule


@dataclass
class Solver(object):
    template: str
    rules: set[Rule]
    iterations: int

    @property
    def solution(self) -> int:
        pairs = list(sliding_window(self.template, 2))
        pair_freqs = frequency_map(pairs)

        for _ in range(self.iterations):
            pair_freqs = self.produce_next(pair_freqs)

        occurrences = self.count_occurrences(pair_freqs)
        frequencies = [count for count in occurrences.values()]
        return max(frequencies) - min(frequencies)

    def produce_next(self, pair_freqs: dict[Pair, int]) -> dict[Pair, int]:
        output: dict[Pair, int] = {}
        for pair, freq in pair_freqs.items():
            new_pairs = self.get_result_of_running_rule(pair)
            for new_pair in new_pairs:
                output[new_pair] = output.get(new_pair, 0) + freq
        return output

    def get_result_of_running_rule(self, pair: Pair) -> list[Pair]:
        rule = self.rule_map.get(pair)
        if rule:
            return [(rule.left, rule.produces), (rule.produces, rule.right)]
        else:
            return [pair]

    def count_occurrences(self, pair_freqs: dict[Pair, int]) -> dict[str, int]:
        output: dict[str, int] = {}

        for pair, freq in pair_freqs.items():
            for value in pair:
                output[value] = output.get(value, 0) + freq

        for value in (self.template_start, self.template_end):
            output[value] = output.get(value, 0) + 1

        return {value: count // 2 for value, count in output.items()}

    @cached_property
    def template_start(self) -> str:
        return self.template[0]

    @cached_property
    def template_end(self) -> str:
        return self.template[-1]

    @cached_property
    def rule_map(self) -> dict[Pair, Rule]:
        output: dict[Pair, Rule] = {}
        for rule in self.rules:
            output[(rule.left, rule.right)] = rule
        return output
