"""
Truncatable Primes
"""

from pe.integer import concat, split
from pe.misc import sieve_of_eratosthenes_fast
from pe.misc import is_prime
from pe.sequences import prime_seq


def is_trucatable_prime(prime):
    single_digit_primes = set([2, 3, 5, 7])
    if prime in single_digit_primes:
        return False

    digits = split(prime)
    if digits[0] not in single_digit_primes or digits[-1] not in single_digit_primes:
        return False

    for i in range(1, len(digits)):
        num1 = concat(digits[i:])
        num2 = concat(digits[:i])

        if not is_prime(num1) or not is_prime(num2):
            return False

    return True


def solve():
    limit = 11

    truncatable_primes = []
    for prime in sieve_of_eratosthenes_fast(1000000):
        if is_trucatable_prime(prime):
            truncatable_primes.append(prime)
            if len(truncatable_primes) == limit:
                break

    return str(sum(truncatable_primes))
