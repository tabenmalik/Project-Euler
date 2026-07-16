from __future__ import annotations

import math
import operator
from functools import reduce

SOLUTION: str = "137846528820"

GRID_SIZE: int = 20


def solve() -> str:
    terms = map(lambda i: (GRID_SIZE + i) / i, range(1, GRID_SIZE + 1))
    prod = reduce(operator.mul, terms)

    return str(math.ceil(prod))
