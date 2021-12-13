from dataclasses import dataclass

from src.utils.point import Point


@dataclass
class FoldX(object):
    value: int


@dataclass
class FoldY(object):
    value: int


Fold = FoldX | FoldY


@dataclass
class Data(object):
    points: set[Point]
    folds: list[Fold]
