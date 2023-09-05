"""
Project Euler problem 006: https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,

(1^2) + (2^2) + ... + (10^2) = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""
from pe.integer import sum_of_1_to_n, sum_of_sqrs



MAX_NUM = 100


def solve():
    """Solves Project Euler problem 006"""
    return str(sum_of_1_to_n(MAX_NUM) ** 2 - sum_of_sqrs(MAX_NUM))
