import unittest

from .sample_data import SAMPLE_DATA
from src.day_06.b import solve


class TestDay06B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA, 256), 26984457539)
