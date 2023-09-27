"""
Largest Prime Factor

.. raw:: html
   :url: https://projecteuler.net/minimal=003

Project Euler problem 003: https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from pe.integer import prime_factors_of_n


NUM = 600_851_475_143


def solve():
    """Solves Project Euler problem 003"""
    prime_factors = prime_factors_of_n(NUM)
    max_prime_factor = max(prime_factors)
    return str(max_prime_factor)
