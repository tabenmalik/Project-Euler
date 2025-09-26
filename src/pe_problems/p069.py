from math import gcd, isqrt
from pe.misc import sieve_of_eratosthenes_fast
from pe.predicates import le
from itertools import takewhile
from functools import reduce
from operator import mul

SOLUTION = "510510"

primes = sieve_of_eratosthenes_fast(1_000_000)


def totient_ratio(n: int) -> int:
    return reduce(mul, (p / (p - 1) for p in takewhile(le(isqrt(n)), primes) if n % p == 0), 1)


def solve() -> str:
    max_ratio = 0
    max_n = 0
    for n in range(1_000_000):
        t = totient_ratio(n)
        if t > max_ratio:
            max_ratio = t
            max_n = n
    return str(max_n)
