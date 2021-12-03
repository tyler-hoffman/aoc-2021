from typing import Dict, List
import unittest
from parameterized import parameterized

from src.utils.collections import frequency_map


class TestFrequencyMap(unittest.TestCase):
    @parameterized.expand(
        [
            ([], {}),
            (["a"], {"a": 1}),
            (["a", "b", "a"], {"a": 2, "b": 1}),
        ]
    )
    def test_frequency_map(self, input: List[str], expected: Dict[str, int]):
        self.assertEqual(frequency_map(input), expected)
