import unittest

from .sample_data import SAMPLE_DATA
from src.day_19.a import solve


class TestDay19A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 1)
