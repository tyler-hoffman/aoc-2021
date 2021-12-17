from functools import cached_property
from src.day_17.models import Trajectory
from src.day_17.parser import Parser
from src.day_17.solver import Solver
from src.utils.point import Point


class Day17PartBSolver(Solver):
    @property
    def solution(self) -> int:
        points = set[Point]()
        for t in self.valid_times:
            ys = self.y_vels_by_time.get(t, {})
            xs = self.x_vels_by_time.get(t, {})

            for y in ys:
                for x in xs:
                    p = Point(x=x, y=y)
                    points.add(p)

        return len(points)

    @cached_property
    def y_vels_by_time(self) -> dict[int, set[int]]:
        return self.vel_t_map_to_t_vel_map(self.times_y_vels_lead_to_target)

    @cached_property
    def x_vels_by_time(self) -> dict[int, set[int]]:
        return self.vel_t_map_to_t_vel_map(self.times_x_vels_lead_to_target)

    @staticmethod
    def vel_t_map_to_t_vel_map(
        vels_to_times: dict[int, set[int]]
    ) -> dict[int, set[int]]:
        output = dict[int, set[int]]()
        for vel, times in vels_to_times.items():
            for t in times:
                if t not in output:
                    output[t] = set()
                output[t].add(vel)
        return output

    @cached_property
    def times_x_vels_lead_to_target(self) -> dict[int, set[int]]:
        output = dict[int, set[int]]()
        for x_vel in range(self.min_x_vel_to_check, self.max_x_vel_to_check + 1):
            output[x_vel] = self.times_x_vel_leads_to_target(x_vel)
        return {k: v for k, v in output.items() if v}

    def times_x_vel_leads_to_target(self, x_vel: int) -> set[int]:
        trajectory = Trajectory(x_vel=x_vel)
        output = set[int]()
        x = 0
        t = -1
        x_points = trajectory.x_points()
        while x <= self.target_area.x_max and t <= self.max_time:
            t += 1
            x = next(x_points)
            if self.target_area.x_min <= x <= self.target_area.x_max:
                output.add(t)

        return output

    @cached_property
    def times_y_vels_lead_to_target(self) -> dict[int, set[int]]:
        output = dict[int, set[int]]()
        for y_vel in range(self.min_y_vel_to_check, self.max_y_vel_to_check + 1):
            output[y_vel] = self.times_y_vel_leads_to_target(y_vel)
        return {k: v for k, v in output.items() if v}

    def times_y_vel_leads_to_target(self, y_vel: int) -> set[int]:
        trajectory = Trajectory(y_vel=y_vel)
        output = set[int]()
        y = 0
        t = -1
        y_points = trajectory.y_points()
        while y >= self.target_area.y_min:
            t += 1
            y = next(y_points)
            if self.target_area.y_min <= y <= self.target_area.y_max:
                output.add(t)
        return output

    @cached_property
    def max_time(self) -> int:
        return max(self.y_vels_by_time.keys())

    @cached_property
    def valid_times(self) -> set[int]:
        times = set[int]()
        times.update(self.y_vels_by_time.keys())
        times.update(self.x_vels_by_time.keys())
        return times


def solve(input: str) -> int:
    parser = Parser()
    solver = Day17PartBSolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_17/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
