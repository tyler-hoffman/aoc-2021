from dataclasses import dataclass

from src.utils.point import Point


@dataclass
class Image(object):
    pixels: set[Point]
    outer_pixels_on: bool
    min_x: int
    min_y: int
    max_x: int
    max_y: int

    def is_pixel_on(self, p: Point) -> bool:
        if self.min_x <= p.x < self.max_x and self.min_y <= p.y < self.max_y:
            return p in self.pixels
        else:
            return self.outer_pixels_on

    def __repr__(self) -> str:
        lines = list[str]()
        ys = list(range(self.min_y, self.max_y))
        xs = list(range(self.min_x, self.max_x))
        for y in ys:
            chars = ["#" if Point(x=x, y=y) in self.pixels else "." for x in xs]
            lines.append("".join(chars))
            
        return "\n".join(lines)
