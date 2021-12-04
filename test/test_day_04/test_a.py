import unittest

from src.day_04.a import solve


class TestDay04A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(input), 1)
