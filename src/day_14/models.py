from dataclasses import dataclass
from functools import cached_property

Pair = tuple[str, str]


@dataclass(frozen=True)
class Rule(object):
    left: str
    right: str
    produces: str

    @cached_property
    def input(self) -> Pair:
        return (self.left, self.right)

    @cached_property
    def output(self) -> tuple[Pair, Pair]:
        return ((self.left, self.produces), (self.produces, self.right))


@dataclass
class Data(object):
    template: str
    rules: set[Rule]
