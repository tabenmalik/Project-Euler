from __future__ import annotations

import math
from collections.abc import Generator
from collections.abc import Sequence

from pe.integer import prime_factors_trial_division
from pe.itertools import sieve


def prime_factorization(n: int) -> tuple[Sequence[int], Sequence[int]]:
    primes = sieve(n)
    prime_divisors = list(filter(lambda x: n % x == 0, primes))

    exps = []
    for prime in prime_divisors:
        exp = 0
        while n % prime == 0:
            exp += 1
            n //= prime
        exps.append(exp)

    return prime_divisors, exps


def prime_factors(num: int) -> Generator[int]:
    return prime_factors_trial_division(num)


def divisors(n: int, sort: bool = False) -> Sequence[int]:
    divisors = [1, n]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.extend([i, int(n / i)])

    if sort:
        divisors = sorted(divisors)

    return tuple(divisors)


PRIME_CACHE: set[int] = set()
MAX_PRIME = 2


def is_prime(num: int) -> bool:
    """
    Returns True if the given number
    """
    global PRIME_CACHE
    global MAX_PRIME

    if num in PRIME_CACHE:
        return True
    elif len(PRIME_CACHE) > 0 and num < MAX_PRIME:
        return False
    elif num <= 1:
        return False

    PRIME_CACHE = set(sieve(3 * num))
    MAX_PRIME = max(PRIME_CACHE)
    return num in PRIME_CACHE
