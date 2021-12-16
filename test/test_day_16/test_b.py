import unittest

from src.day_16.b import solve


class TestDay16B(unittest.TestCase):
    def test_solve(self):
        with open("src/day_16/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input), 194435634456)
