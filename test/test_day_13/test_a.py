import unittest

from .sample_data import SAMPLE_DATA
from src.day_13.a import solve


class TestDay13A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 1)
