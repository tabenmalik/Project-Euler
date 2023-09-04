from functools import reduce
from operator import mul
from itertools import takewhile
from math import isqrt

from project_euler.predicates import le
from project_euler.misc import sieve_of_eratosthenes_fast
from project_euler.integer import split

primes = sieve_of_eratosthenes_fast(1_000_000)

SOLUTION = ''

def totient_ratio(n):
    return reduce(mul, (p / (p-1) for p in takewhile(le(isqrt(n)), primes) if n % p == 0), 1)


def totient(n):
    return n * reduce(mul, (1 - (1/p) for p in takewhile(le(isqrt(n)), primes) if n % p == 0), 1)

def solve():
    for n in range(2, 10**7):
        if sorted(split(int(totient(n)))) == sorted(split(n)):
            pass
