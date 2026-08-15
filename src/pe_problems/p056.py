from __future__ import annotations

from itertools import product

from pe.integer import split

SOLUTION = "972"


def solve() -> str:
    max_digit_sum = 0
    for x, y in product(range(0, 100), range(0, 100)):
        digits = split(x**y)
        max_digit_sum = max(max_digit_sum, sum(digits))

    return str(max_digit_sum)
