from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from math import ceil, floor
from typing import Any, Iterator, Optional


@dataclass
class SnailfishNumber(ABC):
    parent: Optional[SnailfishPair]

    @abstractmethod
    def nodes(self) -> Iterator[SnailfishLeafNode]:
        ...

    @property
    @abstractmethod
    def magnitude(self) -> int:
        ...

    @property
    def depth(self) -> int:
        return 1 + self.parent.depth if self.parent else 0

    def reduce(self) -> None:
        reducing = True
        while reducing:
            reducing = self.reduce_next()

    def reduce_next(self) -> bool:
        return self.reduce_next_explode() or self.reduce_next_split()

    def reduce_next_explode(self) -> bool:
        nodes = self.nodes()
        prev: Optional[SnailfishLeafNode] = None
        curr: Optional[SnailfishLeafNode] = None
        upcoming: Optional[SnailfishLeafNode] = next(nodes)
        after_that: Optional[SnailfishLeafNode] = next(nodes)

        for node in [*nodes, None, None]:
            prev, curr, upcoming, after_that = curr, upcoming, after_that, node
            if curr.depth > 4:
                curr.parent.explode(prev=prev, upcoming=after_that)
                return True
        return False

    def reduce_next_split(self) -> bool:
        for node in self.nodes():
            if node.value >= 10:
                node.parent.split(child=node)
                return True
        return False

    def __add__(self, other: Any) -> SnailfishNumber:
        if not isinstance(other, SnailfishNumber):
            raise Exception(f"Can't add {type(other)} to SnailfishNumber")
        parent = SnailfishPair(parent=None, left=self, right=other)
        self.parent = parent
        other.parent = parent
        parent.reduce()
        return parent

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, SnailfishNumber) and str(self) == str(other)


@dataclass(eq=False)
class SnailfishPair(SnailfishNumber):
    left: SnailfishNumber
    right: SnailfishNumber

    def explode(
        self, prev: Optional[SnailfishLeafNode], upcoming: Optional[SnailfishLeafNode]
    ) -> None:
        parent = self.parent
        assert parent is not None
        assert isinstance(self.left, SnailfishLeafNode)
        assert isinstance(self.right, SnailfishLeafNode)

        if prev is not None:
            prev.value += self.left.value
        if upcoming is not None:
            upcoming.value += self.right.value
        if self == parent.left:
            parent.left = SnailfishLeafNode(parent=parent, value=0)
        elif self == parent.right:
            parent.right = SnailfishLeafNode(parent=parent, value=0)
        else:
            raise Exception(f"How would you manage to get here?")

    def split(self, child: SnailfishLeafNode) -> None:
        left = SnailfishLeafNode(parent=None, value=floor(child.value / 2))
        right = SnailfishLeafNode(parent=None, value=ceil(child.value / 2))
        pair = SnailfishPair(parent=self, left=left, right=right)
        left.parent = pair
        right.parent = pair

        if child == self.left:
            self.left = pair
        elif child == self.right:
            self.right = pair
        else:
            raise Exception(f"Bad child received: {child}")

    def nodes(self) -> Iterator[SnailfishLeafNode]:
        yield from self.left.nodes()
        yield from self.right.nodes()

    @property
    def magnitude(self) -> int:
        return 3 * self.left.magnitude + 2 * self.right.magnitude

    def __repr__(self) -> str:
        return f"[{self.left},{self.right}]"


@dataclass(eq=False)
class SnailfishLeafNode(SnailfishNumber):
    value: int

    def nodes(self) -> Iterator[SnailfishLeafNode]:
        yield self

    @property
    def magnitude(self) -> int:
        return self.value

    def __repr__(self) -> str:
        return f"{self.value}"
