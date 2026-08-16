from __future__ import annotations

import math
from itertools import product

from pe.integer import sum_of_1_to_n

SOLUTION = "4179871"
MAX_NUM = 28123


def proper_divisors(n: int) -> list[int]:
    if n == 1:
        return []
    divisors = []
    divisors.append(1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            j = n // i
            if j != i:
                divisors.append(j)
    return sorted(divisors)


def is_abundant(n: int) -> int:
    return sum(proper_divisors(n)) > n


def solve() -> str:
    abundant_nums = tuple(
        n
        for n in range(2, MAX_NUM + 1)
        if is_abundant(n)
    )

    abundant_sums = tuple(
        a + b
        for a, b in product(abundant_nums, repeat=2)
        if a + b <= MAX_NUM
    )

    non_abundant_sum = sum_of_1_to_n(MAX_NUM) - sum(set(abundant_sums))
    return str(non_abundant_sum)
