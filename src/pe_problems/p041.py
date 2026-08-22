from __future__ import annotations

from itertools import permutations

from pe.integer import concat
from pe.integer import count_digits
from pe.integer import split
from pe.itertools import sieve

SOLUTION = "7652413"


def solve() -> str:
    # omitting digits 8 and 9 since all 8-digit and 9-digit
    # pandigital numbers are not prime
    # sum(range(9)) -> divisible by 3
    # sum(range(10)) -> divisible by 9
    largest = 7654321
    primes = {
        prime
        for prime in sieve(largest)
        if prime >= 10**(count_digits(largest) - 1)
    }
    for pandigital_digits in permutations(split(largest)):
        pandigital = concat(pandigital_digits)
        if pandigital in primes:
            return str(pandigital)

    raise AssertionError('unreachable')
