from __future__ import annotations

import os
from collections.abc import Iterable
from importlib.resources import files
from math import log

import pe_problems

SOLUTION: str = "709"


def argmax(iterable: Iterable[int]) -> int:
    it = iter(iterable)

    maxi = 0
    maxn = next(it)

    for i, n in enumerate(it, 1):
        if n > maxn:
            maxn = n
            maxi = i

    return maxi


def solve() -> str:
    this_dir, _ = os.path.split(__file__)

    lines = files(pe_problems).joinpath("p099.txt").read_text().splitlines()

    max_val = 0.0
    argmax = 0
    for i, line in enumerate(lines, 1):
        x, e = map(int, line.split(","))
        val = e * log(x)
        if val > max_val:
            max_val = val
            argmax = i

    return str(argmax)


if __name__ == "__main__":
    print(solve())
