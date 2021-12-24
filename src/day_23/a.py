from dataclasses import dataclass, field
from queue import PriorityQueue
from src.day_23.models import GameState
from src.day_23.parser import Parser
from src.day_23.solver import Solver


infinity = float("inf")


@dataclass
class Day23PartASolver(Solver):
    start_state: GameState
    marked: dict[GameState, int] = field(default_factory=dict)
    state_queue: PriorityQueue[tuple[int, GameState]] = field(
        default_factory=PriorityQueue
    )

    @property
    def solution(self) -> int:
        self.add_to_queue(self.start_state)
        while True:
            _, state = self.state_queue.get()
            if state.done:
                return state.cost_so_far
            else:
                self.expand(state)

    def expand(self, game_state: GameState) -> None:
        for state in game_state.potential_new_states():
            if state.optimistic_total_cost < self.marked.get(state, infinity):
                self.add_to_queue(state)

    def add_to_queue(self, state: GameState) -> None:
        self.marked[state] = state.optimistic_total_cost
        self.state_queue.put((state.optimistic_total_cost, state))


def solve(input: str) -> int:
    start_state = Parser.parse(input)
    solver = Day23PartASolver(start_state=start_state)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_23/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
