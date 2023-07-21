"""
"""
from fractions import Fraction
from functools import reduce
from itertools import count, islice

from project_euler.integer import split

SOLUTION = '272'

def continued_frac_coeffs_for_e():
    yield 2

    for i in count(1):
        yield 1
        yield 2 * i
        yield 1


def continued_fraction_op(a, b):
    return (1 / Fraction(a)) + Fraction(b)

def solve():
    """
    """
    coeffs = list(islice(continued_frac_coeffs_for_e(), 100))
    nth_convergent = reduce(continued_fraction_op, list(reversed(coeffs)))
    return str(sum(split(nth_convergent.numerator)))
    
