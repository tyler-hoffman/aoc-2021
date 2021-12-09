import unittest

from .sample_data import SAMPLE_DATA
from src.day_09.b import solve


class TestDay09B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 1134)
