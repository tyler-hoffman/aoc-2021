import unittest

from .sample_data import SAMPLE_DATA
from src.day_18.a import solve


class TestDay18A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 4140)
