from __future__ import annotations

from pe.integer import concat
from pe.integer import ireversed
from pe.integer import palindromic
from pe.integer import split

SOLUTION = "249"


def is_lychrel(n: int, iterations: int = 50) -> bool:
    num = n
    for _ in range(0, iterations):
        num += ireversed(num)
        if palindromic(num):
            return False

    return True


def solve() -> str:
    lychrel_nums = list(filter(is_lychrel, range(1, 10_000)))
    return str(len(lychrel_nums))
