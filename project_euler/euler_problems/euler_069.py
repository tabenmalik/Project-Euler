from math import gcd, isqrt
from project_euler.misc import sieve_of_eratosthenes_fast
from project_euler.predicates import le
from itertools import takewhile
from functools import reduce
from operator import mul
SOLUTION = ''

primes =  sieve_of_eratosthenes_fast(1_000_000)

def totient_ratio(n):
    return reduce(mul, (p / (p-1) for p in takewhile(le(isqrt(n)), primes) if n % p == 0), 1)

def solve():
    pass
