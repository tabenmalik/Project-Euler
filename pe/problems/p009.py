"""
Project Euler problem 009: https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from pe.integer import product
from pe.more_itertools import first_true
from pe.more_itertools import arg_expander


SUM_NUM = 1000


def is_pythagorean_triplet(a, b, c):
    """A predicate that returns True if a, b, c is a Pythagorean Triplet"""
    return ((a**2) + (b**2)) == (c**2)


def solve():
    """Solves Project Euler problem 009"""

    sum_triplets = (
        (a, b, SUM_NUM - a - b)
        for a in range(1, SUM_NUM)
        for b in range(a + 1, SUM_NUM - a)
    )

    pred_pythagorean_triplet = arg_expander(is_pythagorean_triplet)
    pythagorean_triplet = first_true(sum_triplets, pred=pred_pythagorean_triplet)
    prod_of_triplet = product(*pythagorean_triplet)

    return str(prod_of_triplet)
