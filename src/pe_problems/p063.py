from itertools import count, takewhile
from typing import Iterable

from pe.integer import split

SOLUTION = "49"


def positive_integers_seq(start: int = 1, step: int = 1) -> Iterable[int]:
    return count(start, step)


def solve() -> str:
    n = 1
    total = 0
    while True:
        nums = map(lambda i: i**n, positive_integers_seq())
        nums = takewhile(lambda num: len(split(num)) <= n, nums)
        nums = filter(lambda num: len(split(num)) == n, nums)

        subtotal = len(list(nums))
        if subtotal == 0:
            break
        total += subtotal
        n += 1

    return str(total)
