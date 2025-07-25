"""
Project Euler problem 001: https://projecteuler.net/problem=1

Description:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

SOLUTION = "233168"


def solve():
    """Solves Project Euler problem 001"""
    MAX_NUM = 1000
    num_3s = range(0, MAX_NUM, 3)
    num_5s = range(0, MAX_NUM, 5)
    num_15s = range(0, MAX_NUM, 15)

    total = sum(num_3s) + sum(num_5s) - sum(num_15s)

    return str(total)
