from __future__ import annotations

import operator
from functools import reduce

SOLUTION: str = "648"


MAX_NUM: int = 100


def solve() -> str:
    product = reduce(operator.mul, range(1, MAX_NUM + 1))
    product_str = str(product)
    product_digits = list(map(int, product_str))
    return str(sum(product_digits))
