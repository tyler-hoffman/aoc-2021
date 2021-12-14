from dataclasses import dataclass
from functools import cached_property
from more_itertools import sliding_window

from src.utils.collections import frequency_map
from src.day_14.models import Pair, Rule


@dataclass
class Solver(object):
    """Solver for day 14

    The trick here is representing the string at any given iteration
    as a frequency map of pairs of adjacent characters.

    So AAAB internally is {("A", "A"): 2, ("A", "B"): 1}

    Then for the next iteration, we apply the rule to each key.
    So for ("A", "A"), we find the corresponding rule, which produces
    2 new pairs. And since the frequency of this was 2, we know we have
    2 of each of those pairs.

    This works because we never care about the position
    of any character or pair of characters.

    Also, we got away with not doing a few null checks because we
    seem to have a rule for any possible pair.

    Runtime: O(MN)
    Where    M = self.iterations
             N = len(self.rules)
    """

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
        output: dict[str, int] = {pair: 0 for pair in self.all_pairs}
        for pair, freq in pair_freqs.items():
            new_pairs = self.rule_map[pair].output
            for new_pair in new_pairs:
                output[new_pair] += freq
        return output

    def count_occurrences(self, pair_freqs: dict[Pair, int]) -> dict[str, int]:
        """Compute frequency of each character in a string represented by pairs

        Takes a frequency list of frequencies of pairs and computes the number of each
        character in the string they represent. Since all characters except the first
        and last are present in both the left and right of a tuple, they are represented twice.

        So...
         - iterate through pairs, and increment count for both left and right value
         - now we have double counted all but the first and last character
         - increment the count for the first and last so that ALL characters are double counted
         - divide all counts by 2 to get their true count
        """
        output: dict[str, int] = {pair: 0 for pair in self.all_characters}

        for pair, freq in pair_freqs.items():
            for value in pair:
                output[value] += freq

        for value in (self.template[0], self.template[-1]):
            output[value] += 1

        return {value: count // 2 for value, count in output.items()}

    @cached_property
    def rule_map(self) -> dict[Pair, Rule]:
        return {rule.input: rule for rule in self.rules}

    @cached_property
    def all_characters(self) -> set[str]:
        output = set[str]()
        for rule in self.rules:
            output.add(rule.left)
            output.add(rule.right)
            output.add(rule.produces)
        return output

    @cached_property
    def all_pairs(self) -> set[str]:
        return self.rule_map.keys()
