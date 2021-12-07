from dataclasses import dataclass


@dataclass
class Direction(object):
    value: int


class Up(Direction):
    pass


class Down(Direction):
    pass


class Forward(Direction):
    pass
