from __future__ import annotations

from collections.abc import Generator

from pe.integer import concat
from pe.integer import split
from pe.itertools import sieve

SOLUTION = "55"


def cycle_digits(num: int) -> Generator[int]:
    yield num

    digits = list(split(num))
    digits = digits[1:] + digits[:1]
    new_num = concat(digits)
    while new_num != num:
        yield new_num
        digits = digits[1:] + digits[:1]
        new_num = concat(digits)


def solve() -> str:
    limit = 1_000_000
    primes = set(sieve(limit))

    num_cycles = map(lambda x: (x, set(cycle_digits(x))), primes)
    prime_cycles = filter(lambda x: x[1].issubset(primes), num_cycles)
    return str(len(list(prime_cycles)))
