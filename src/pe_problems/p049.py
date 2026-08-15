from __future__ import annotations

from collections import defaultdict
from collections.abc import Sequence
from itertools import combinations

from pe.integer import concat
from pe.integer import split
from pe.itertools import sieve

SOLUTION = "296962999629"


def differences(ints: Sequence[int]) -> list[int]:
    d = []
    for i in range(1, len(ints)):
        d.append(ints[i - 1] - ints[i])

    return d


SortedDigits = tuple[int, ...]
Primes = list[int]


def solve() -> str:
    num_terms = 3
    existing_sequence = (1487, 4817, 8147)

    # primes with only 4 digits
    primes = tuple(prime for prime in sieve(10000) if prime >= 1000)

    primes_by_digits: dict[SortedDigits, Primes] = defaultdict(list)
    for prime in primes:
        digits = tuple(sorted(split(prime)))
        primes_by_digits[digits].append(prime)

    for prime_family in primes_by_digits.values():
        if len(prime_family) < num_terms:
            continue

        for sequence in combinations(prime_family, num_terms):
            if (
                len(set(differences(sequence))) == 1
                and sequence != existing_sequence
            ):
                return str(concat(sequence))

    raise AssertionError('unreachable')
