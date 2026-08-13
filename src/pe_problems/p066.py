from __future__ import annotations

import math
from fractions import Fraction

SOLUTION = "661"


def issquare(x: int) -> bool:
    return math.isqrt(x) ** 2 == x


Triple = tuple[int, int, int]


def next_triple(t: Triple, N: int) -> Triple:
    m = 1

    while Fraction((t[0] + t[1] * m), t[2]).denominator != 1:
        m += 1
    a = (t[0] * m + N * t[1]) // abs(t[2])
    b = (t[0] + t[1] * m) // abs(t[2])
    c = (m * m - N) // t[2]
    return (a, b, c)


def min_dio(D: int) -> Triple:
    a = int(math.isqrt(D) + 1)
    t = (a, 1, a * a - D)
    while t[2] != 1:
        t = next_triple(t, D)
    return t


def solve() -> str:
    max_x = 0
    max_D = 0
    for D in range(2, 1001):
        if issquare(D):
            continue
        t = min_dio(D)
        if t[0] > max_x:
            max_x = t[0]
            max_D = D
    return str(max_D)
