"""
Amicable Numbers

.. raw:: html
   :url: https://projecteuler.net/minimal=021
"""

import math


MAX_NUM = 10_000


def proper_divisors(n):
    if n == 1:
        return []

    divisors = []
    divisors.append(1)
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    return sorted(divisors)


def is_amicable(n):
    b = sum(proper_divisors(n))
    d_b = sum(proper_divisors(b))

    return n == d_b and n != b


def solve():
    amicable_nums = list(filter(is_amicable, range(2, MAX_NUM)))
    return str(sum(amicable_nums))
