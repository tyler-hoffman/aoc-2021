from abc import ABC
from dataclasses import dataclass
from itertools import product
from typing import Iterator

from src.day_20.models import Image
from src.utils.point import Point


@dataclass
class Solver(ABC):
    algorithm: list[bool]
    input_image: Image

    def enhancements(self) -> Iterator[Image]:
        image = self.input_image
        yield image
        while True:
            image = self.enhance(image)
            yield image

    def enhance(self, image: Image) -> Image:
        min_x = image.min_x - 1
        min_y = image.min_y - 1
        max_x = image.max_x + 1
        max_y = image.max_y + 1

        new_pixels = set[Point]()
        xs = range(min_x, max_x)
        ys = range(min_y, max_y)
        if image.outer_pixels_on:
            new_outer_pixels = self.algorithm[-1]
        else:
            new_outer_pixels = self.algorithm[0]
        for y, x in product(ys, xs):
            point = Point(x=x, y=y)
            if self.next_pixel_is_on(image, point):
                new_pixels.add(point)

        return Image(
            pixels=new_pixels,
            outer_pixels_on=new_outer_pixels,
            min_x=min_x,
            max_x=max_x,
            min_y=min_y,
            max_y=max_y,
        )

    def next_pixel_is_on(self, image: Image, point: Point) -> bool:
        neighbors = self.neighbors(image, point)
        reversed = neighbors[::-1]
        index = sum([int(exists) * 2 ** i for i, exists in enumerate(reversed)])
        return self.algorithm[index]

    @staticmethod
    def neighbors(image: Image, point: Point) -> list[bool]:
        ys = range(point.y - 1, point.y + 2)
        xs = range(point.x - 1, point.x + 2)
        points = [Point(x=x, y=y) for y, x in product(ys, xs)]

        return [image.is_pixel_on(p) for p in points]
