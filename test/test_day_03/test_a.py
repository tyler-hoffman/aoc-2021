import unittest

from src.day_03.a import solve


class TestDay03A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(input), 1)
