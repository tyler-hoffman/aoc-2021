from dataclasses import dataclass

from src.utils.point import Point


@dataclass
class Image(object):
    pixels: set[Point]
    min_x: int
    min_y: int
    max_x: int
    max_y: int

    def __repr__(self) -> str:
        lines = list[str]()
        ys = list(range(self.min_y, self.max_y))
        xs = list(range(self.min_x, self.max_x))
        for y in ys:
            chars = ["#" if Point(x=x, y=y) in self.pixels else "." for x in xs]
            lines.append("".join(chars))
            
        return "\n".join(lines)
