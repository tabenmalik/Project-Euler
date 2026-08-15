from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterator
from itertools import count

from pe.integer import split

SOLUTION = "127035954683"


def n_digit_cubes(n: int) -> Iterator[int]:
    start = int(10 ** ((n - 1) / 3)) + 1
    for x in count(start):
        cube = x ** 3
        if len(split(cube)) > n:
            break
        yield cube


SortedDigits = tuple[int, ...]
Permutations = list[int]
GroupedPermutations = dict[SortedDigits, Permutations]


def solve() -> str:
    target_group_size = 5

    for n_digits in count(1):
        permutatation_groups: GroupedPermutations = defaultdict(list)

        for cube in n_digit_cubes(n_digits):
            digits_key = tuple(sorted(split(cube)))
            permutation_group = permutatation_groups[digits_key]
            permutation_group.append(cube)

            if len(permutation_group) == target_group_size:
                return str(min(permutation_group))

    raise AssertionError('Should never get here')
