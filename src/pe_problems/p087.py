from __future__ import annotations

import math

from pe.itertools import sieve

SOLUTION: str = "1097343"


def solve() -> str:
    primes = list(sieve(math.isqrt(50_000_000)))

    nums = set()
    for p1 in primes:
        for p2 in primes:
            for p3 in primes:
                n = p1**2 + p2**3 + p3**4
                if n >= 50_000_000:
                    break
                nums.update([n])

    return str(len(nums))
