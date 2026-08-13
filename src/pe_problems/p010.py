"""Project Euler problem 010: https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from __future__ import annotations

from pe.itertools import sieve

SOLUTION: str = "142913828922"

MAX_NUM: int = 2_000_000


def solve() -> str:
    """Solves Project Euler problem 010"""
    return str(sum(sieve(MAX_NUM)))
