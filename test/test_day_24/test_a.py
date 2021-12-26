import unittest

from src.day_24.a import solve


class TestDay24A(unittest.TestCase):
    def test_solve(self):
        with open("src/day_24/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input), 99995969919326)
