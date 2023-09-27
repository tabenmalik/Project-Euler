"""
Digit Cancelling Fractions

.. raw:: html
   :url: https://projecteuler.net/minimal=033
"""

from itertools import starmap
from functools import reduce
import operator

from pe.integer import split, concat
from pe.misc import prime_factors


def is_wrongly_canceled(numerator, denominator):
    num_digits = split(numerator)
    den_digits = split(denominator)

    for digit in num_digits:
        if digit in den_digits and digit != 0:
            new_num = list(num_digits)
            new_num.remove(digit)
            new_num = concat(new_num)

            new_den = list(den_digits)
            new_den.remove(digit)
            new_den = concat(new_den)

            if new_den != 0 and (numerator / denominator) == (new_num / new_den):
                return True

    return False


def solve():
    fractions = [(i, j) for i in range(10, 100) for j in range(i + 1, 100)]
    bad_fractions = filter(lambda x: is_wrongly_canceled(*x), fractions)
    bad_fractions = list(bad_fractions)

    num_prod, den_prod = tuple(zip(*bad_fractions))
    num_prod = reduce(operator.mul, num_prod)
    den_prod = reduce(operator.mul, den_prod)

    num_factors = list(prime_factors(num_prod))
    den_factors = list(prime_factors(den_prod))
    new_num_factors = list()
    for num in num_factors:
        if num in den_factors:
            den_factors.remove(num)
        else:
            new_num_factors.append(num)

    if len(new_num_factors) == 0:
        new_num_factors.append(1)

    den_prod = reduce(operator.mul, den_factors)
    return str(den_prod)
