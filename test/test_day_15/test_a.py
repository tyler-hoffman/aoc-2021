import unittest

from .sample_data import SAMPLE_DATA
from src.day_15.a import solve


class TestDay15A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 1)
