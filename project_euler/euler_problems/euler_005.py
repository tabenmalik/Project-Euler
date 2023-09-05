"""
Project Euler problem 005: https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of
the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from itertools import takewhile
import math

from project_euler.sequences import prime_seq
from project_euler.predicates import lt



MAX_NUM = 20

def solve():
    """Solves Project Euler problem 005"""
    primes = prime_seq()
    primes = takewhile(lt(MAX_NUM + 1), primes)

    product = 1
    for prime in primes:
        exp = 1
        if prime * prime <= MAX_NUM:
            exp = int(math.log(MAX_NUM) // math.log(prime))
        product *= prime ** exp

    return str(product)
