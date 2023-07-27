from math import isqrt
from itertools import count, takewhile, islice
from typing import Generator

from pe.predicates import le

SOLUTION = ""

def squares(start: int = 1) -> Generator[int, None, None]:
    for i in count(start):
        yield i**2


def nonsquares() -> Generator[int, None, None]:
    for i in count(2):
        if isqrt(i) ** 2 != i:
            yield i


def diophantine_min_x(D: int) -> int:
    for m in squares():
        print("m:", m)
        d = m * D + 1
        if isqrt(d) ** 2 == d:
            return int(isqrt(d))
    raise Exception("Not expected")


def solve() -> str:
    maxx = 3
    maxD = 2

    for D in takewhile(le(1000), nonsquares()):
        x = diophantine_min_x(D)
        print(D, x)
        if x > maxx:
            maxx = x
            maxD = D

    return str(maxD)
