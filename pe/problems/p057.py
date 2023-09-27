"""
Square Root Convertgents

.. raw:: html
   :url: https://projecteuler.net/minimal=057
"""

from functools import reduce
import operator
from pe.integer import split


def memoize(func):
    results = {}

    def _memoized_func(*args):
        if args in results:
            return results[args]

        result = func(*args)
        results[args] = result
        return result

    return _memoized_func


@memoize
def prime_factors(num):
    factor = 2

    while factor * factor <= num:
        if num % factor == 0:
            return [factor] + prime_factors(num // factor)
        else:
            factor += 1

    return [1, num]


def reduce_fraction(frac):
    num_factors = list(prime_factors(frac[0]))
    den_factors = list(prime_factors(frac[1]))

    new_num_factors = []
    for num in num_factors:
        if num in den_factors:
            den_factors.remove(num)
        else:
            new_num_factors.append(num)

    return (
        reduce(operator.mul, new_num_factors, 1),
        reduce(operator.mul, den_factors, 1),
    )


def add_fractions(f1, f2):
    if isinstance(f1, int):
        f1 = (f1, 1)

    if isinstance(f2, int):
        f2 = (f2, 1)

    return (f1[0] * f2[1] + f2[0] * f1[1], f1[1] * f2[1])


@memoize
def expand_root_2_fractional(iterations):
    if iterations == 1:
        return (1, 2)

    result = add_fractions(2, expand_root_2_fractional(iterations - 1))
    result = tuple(reversed(result))
    return result


def expand_root_2(iterations):
    return add_fractions(1, expand_root_2_fractional(iterations))


def solve():
    expanded_fracs = map(expand_root_2, range(1, 1_001))
    frac_digits = map(lambda frac: (split(frac[0]), split(frac[1])), expanded_fracs)
    frac_digits = map(lambda frac: (len(frac[0]), len(frac[1])), frac_digits)
    frac_digits = filter(lambda frac: frac[0] > frac[1], frac_digits)

    return str(len(list(frac_digits)))
