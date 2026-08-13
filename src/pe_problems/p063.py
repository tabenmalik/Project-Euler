from __future__ import annotations

from collections.abc import Iterator
from itertools import count

from pe.integer import split

SOLUTION = "49"


def n_digit_nth_powers(n: int) -> Iterator[int]:
    for x in count(1):
        num = x**n

        digit_count = len(split(num))
        if digit_count == n:
            yield num
        elif digit_count > n:
            break


def solve() -> str:
    n = 1
    total = 0
    for n in count(1):
        nums = tuple(n_digit_nth_powers(n))
        if not nums:
            break
        total += len(nums)

    return str(total)
