import unittest

from .sample_data import SAMPLE_DATA
from src.day_20.a import solve


class TestDay20A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 35)
