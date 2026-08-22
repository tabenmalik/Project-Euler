from __future__ import annotations

from pe.integer import count_digits
from pe.integer import split
from pe.misc import is_prime
from pe.sequences import prime_seq

SOLUTION = "121313"


def replace_digit(num: int, old: int, new: int) -> int:
    return int(str(num).replace(str(old), str(new)))


def prime_family(prime: int, digit: int) -> tuple[int, ...]:
    prime_len = count_digits(prime)
    family = []
    for new_digit in range(10):
        num = replace_digit(prime, digit, new_digit)
        if count_digits(num) == prime_len and is_prime(num):
            family.append(num)

    return tuple(family)


def solve() -> str:
    for prime in prime_seq():
        for digit in set(split(prime)):
            family = prime_family(prime, digit)
            if len(family) == 8:
                return str(prime)

    raise AssertionError('should never get here')
