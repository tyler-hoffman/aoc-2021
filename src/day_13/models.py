from dataclasses import dataclass

from src.utils.point import Point

@dataclass
class FoldX(object):
    x: int

@dataclass
class FoldY(object):
    y: int

Fold = FoldX | FoldY

@dataclass
class Data(object):
    points: set[Point]
    folds: list[Fold]
