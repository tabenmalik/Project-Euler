from __future__ import annotations

import math
from itertools import count
from itertools import repeat

from pe.integer import concat
from pe.integer import split

SOLUTION = "40730"


def digit_factorial_sum(num: int) -> int:
    digits = split(num)
    digit_factorials = map(math.factorial, digits)
    return sum(digit_factorials)


def find_max() -> int:
    # for an n-digit number the max factorial sum
    # will be sum(9! * n). if the max n-digit number
    # exeeds the max n-digit factorial sum then
    # the factorial sum will always be less for larger numbers
    max_factorial_sum = 0

    for num_digits in count(2):
        max_factorial_sum = num_digits * math.factorial(9)
        num = concat(repeat(9, num_digits))
        if max_factorial_sum < num:
            break

    return max_factorial_sum


def solve() -> str:
    limit = find_max()

    total = 0
    for n in range(10, limit):
        fact_sum = digit_factorial_sum(n)
        if n == fact_sum:
            total += n

    return str(total)
