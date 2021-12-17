import unittest

from .sample_data import SAMPLE_DATA
from src.day_17.b import solve


class TestDay17B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 112)
