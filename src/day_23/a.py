from dataclasses import dataclass, field
from queue import PriorityQueue
from src.day_23.models import GameState
from src.day_23.parser import Parser
from src.day_23.solver import Solver


@dataclass
class Day23PartASolver(Solver):
    start_state: GameState
    marked: set[GameState] = field(default_factory=set)
    state_queue: PriorityQueue[GameState] = field(default_factory=PriorityQueue)

    @property
    def solution(self) -> int:
        self.add_to_queue(self.start_state)
        while True:
            state = self.state_queue.get()
            if state.done:
                return state.cost
            else:
                self.expand(state)

    def expand(self, game_state: GameState) -> None:
        for state in game_state.potential_new_states():
            if state not in self.marked:
                self.add_to_queue(state)

    def add_to_queue(self, state: GameState) -> None:
        self.marked.add(state)
        self.state_queue.put(state)


def solve(input: str) -> int:
    start_state = Parser.parse(input)
    solver = Day23PartASolver(start_state=start_state)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_23/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
