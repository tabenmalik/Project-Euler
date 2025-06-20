from functools import reduce
from operator import mul
from itertools import takewhile
from math import isqrt, gcd
import math

from pe.predicates import le
from pe.misc import sieve_of_eratosthenes_fast, prime_factorization
from pe.integer import split, isperm

primes = sieve_of_eratosthenes_fast(1_000_000)


def totient_ratio(n):
    return reduce(
        mul, (p / (p - 1) for p in takewhile(le(isqrt(n)), primes) if n % p == 0), 1
    )


def is_totient_perm(n):
    num_digits = len(str(n))
    # Initialize result as n
    result = n; 

    # Consider all prime factors
    # of n and subtract their
    # multiples from result
    p = 2; 
    while p * p <= n:
        
        # Check if p is a 
        # prime factor.
        if n % p == 0: 
            
            # If yes, then 
            # update n and result
            while n % p == 0:
                n = n // p
            result -= result // p
            if int(math.log10(result)) != num_digits:
                return False 
        p += 1

    # If n has a prime factor
    # greater than sqrt(n)
    # (There can be at-most 
    # one such prime factor)
    if n > 1:
        result -= int(result / n)
    return isperm(n, result)


def solve():
    global primes
    primes = set(primes)
    for n in range(2, 10**7):
        if n % 1_000_000 == 0:
            print(n)
        is_totient_perm(n)
