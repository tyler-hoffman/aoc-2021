from dataclasses import dataclass
from .point import Point

@dataclass(frozen=True)
class Line(object):
    a: Point
    b: Point

    @property
    def is_vertical(self) -> bool:
        return self.a.x == self.b.x

    @property
    def is_horizontal(self) -> bool:
        return self.a.y == self.b.y
