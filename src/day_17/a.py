from dataclasses import dataclass
from src.day_17.models import TargetArea, Trajectory
from src.day_17.parser import Parser
from src.day_17.solver import Solver


class Day17PartASolver(Solver):
    @property
    def solution(self) -> int:
        trajectory = Trajectory(y_vel=self.max_y_vel_to_check)

        highest_y = 0
        for y in trajectory.y_points():
            if y < highest_y:
                return highest_y
            else:
                highest_y = y


def solve(input: str) -> int:
    target_area = Parser.parse(input)
    solver = Day17PartASolver(target_area=target_area)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_17/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
