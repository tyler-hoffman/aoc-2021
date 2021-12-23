import unittest

from .sample_data import SAMPLE_DATA
from src.day_23.a import solve


class TestDay23A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 12521)
