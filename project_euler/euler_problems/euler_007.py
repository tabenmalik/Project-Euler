"""
Project Euler problem 006: https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from project_euler.more_itertools import nth
from project_euler.sequences import prime_seq

SOLUTION = '104743'

MAX_NUM = 10_001


def solve():
    """Solves Project Euler problem 007"""
    primes = prime_seq()
    last_prime = nth(primes, MAX_NUM)
    return str(last_prime)
