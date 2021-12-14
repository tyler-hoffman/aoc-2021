from dataclasses import dataclass

Pair = tuple[str, str]


@dataclass(frozen=True)
class Rule(object):
    left: str
    right: str
    produces: str


@dataclass
class Data(object):
    template: str
    rules: set[Rule]
