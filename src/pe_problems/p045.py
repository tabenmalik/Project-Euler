from typing import cast

from pe.sequences import Hexagonals, Pentagonals, Triangulars

SOLUTION = "1533776805"


def solve() -> str:
    n = 144
    hexagonals = Hexagonals()
    pentagonals = Pentagonals()
    triangulars = Triangulars()

    while True:
        h = hexagonals[n]
        if cast(int, hexagonals[n]) in pentagonals and h in triangulars:
            return str(h)
        n += 1
