from __future__ import annotations

from collections.abc import Iterator
from itertools import permutations

from pe.integer import concat

SOLUTION = "45228"

Partition = tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]


def partitions(digits: tuple[int, ...]) -> Iterator[Partition]:
    # not a generalized partitioning.
    for i in range(1, 5):
        for j in range(i + 1, 6):
            yield (
                tuple(digits[0:i]),
                tuple(digits[i:j]),
                tuple(digits[j:]),
            )


def solve() -> str:
    digits = tuple(range(1, 10))

    products: set[int] = set()
    for permutation in permutations(digits):
        for partition in partitions(permutation):
            multiplicand = concat(partition[0])
            multiplier = concat(partition[1])
            product = concat(partition[2])

            if multiplicand * multiplier == product:
                products.add(product)

    return str(sum(products))
