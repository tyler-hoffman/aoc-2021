TEST_PART_TEMPLATE = """
import unittest
from parameterized import parameterized

from src.day_{day_string}.{part} import solve


class TestDay{day_string}{part}(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(input), 1)

"""
