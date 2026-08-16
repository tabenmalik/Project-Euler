"""
Project Euler problem 005: https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of
the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
"""
from __future__ import annotations

import math

from pe.itertools import sieve

SOLUTION = "232792560"
MAX_NUM = 20


def solve() -> str:
    """Solves Project Euler problem 005"""
    product = 1
    for prime in sieve(MAX_NUM + 1):
        exp = 1
        if prime * prime <= MAX_NUM:
            exp = int(math.log(MAX_NUM) // math.log(prime))
        product *= prime**exp

    return str(product)
