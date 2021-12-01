from typing import List, Tuple
import unittest
from parameterized import parameterized

from src.utils.iterators import sliding_window


class TestSlidingWindow(unittest.TestCase):
    @parameterized.expand(
        [
            ([2, 3, 5], 1, [(2,), (3,), (5,)]),
            ([2, 3, 5, 7], 2, [(2, 3), (3, 5), (5, 7)]),
            ([2, 3, 5, 7], 3, [(2, 3, 5), (3, 5, 7)]),
        ]
    )
    def test_sliding_window(
        self, input: List[int], size: int, expected: List[Tuple[int, ...]]
    ):
        output = sliding_window(input, size)

        self.assertEqual(list(output), expected)
