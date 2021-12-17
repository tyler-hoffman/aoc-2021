import unittest
from parameterized import parameterized

from src.day_17.models import Trajectory


class TestTrajectory(unittest.TestCase):
    @parameterized.expand(
        [
            (0, [0, 0, 0, 0]),
            (3, [0, 3, 5, 6, 6, 6]),
        ]
    )
    def test_x_at(self, x_vel: int, positions: list[int]):
        trajectory = Trajectory(x_vel=x_vel)
        for t, expected in enumerate(positions):
            self.assertEqual(trajectory.x_at(t), expected)

    @parameterized.expand(
        [
            (2, [0, 2, 3, 3, 2, 0, -3]),
            (3, [0, 3, 5, 6, 6]),
        ]
    )
    def test_y_at(self, y_vel: int, positions: list[int]):
        trajectory = Trajectory(y_vel=y_vel)
        for t, expected in enumerate(positions):
            self.assertEqual(trajectory.y_at(t), expected)
