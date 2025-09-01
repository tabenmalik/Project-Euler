""" """

from fractions import Fraction
from functools import reduce
from itertools import count, islice
from typing import Generator

from pe.integer import split

SOLUTION = "272"


def continued_frac_coeffs_for_e() -> Generator[int, None, None]:
    yield 2

    for i in count(1):
        yield 1
        yield 2 * i
        yield 1


def continued_fraction_op(a: Fraction, b: Fraction) -> Fraction:
    return (1 / a) + b


def solve() -> str:
    """ """
    coeffs = list(islice(continued_frac_coeffs_for_e(), 100))
    nth_convergent = reduce(continued_fraction_op, map(Fraction, list(reversed(coeffs))))
    return str(sum(split(nth_convergent.numerator)))
