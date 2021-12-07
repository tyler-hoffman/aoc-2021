import unittest

from .sample_data import SAMPLE_DATA
from src.day_07.b import solve


class TestDay07B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 168)
