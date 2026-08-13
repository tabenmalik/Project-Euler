from __future__ import annotations

from functools import reduce
from itertools import takewhile
from math import isqrt
from operator import mul

from pe.itertools import sieve
from pe.predicates import le

SOLUTION = "510510"

primes = tuple(sieve(1_000_000))


def totient_ratio(n: int) -> int:
    return reduce(
        mul,
        (p / (p - 1) for p in takewhile(le(isqrt(n)), primes) if n % p == 0),
        1,
    )


def solve() -> str:
    max_ratio = 0
    max_n = 0
    for n in range(1_000_000):
        t = totient_ratio(n)
        if t > max_ratio:
            max_ratio = t
            max_n = n
    return str(max_n)
