"""
10001st Prime

Project Euler problem 007: https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from pe.more_itertools import nth
from pe.sequences import prime_seq


MAX_NUM = 10_001


def solve():
    """Solves Project Euler problem 007"""
    primes = prime_seq()
    last_prime = nth(primes, MAX_NUM - 1)
    return str(last_prime)
