from project_euler.misc import num_to_digits, digits_to_num, prime_factors
from itertools import starmap
from functools import reduce
import operator

SOLUTION = 100

def is_wrongly_canceled(numerator, denominator):
    num_digits = num_to_digits(numerator)
    den_digits = num_to_digits(denominator)

    for digit in num_digits:
        if digit in den_digits and digit != 0:
            new_num = num_digits.copy()
            new_num.remove(digit)
            new_num = digits_to_num(new_num)

            new_den = den_digits.copy()
            new_den.remove(digit)
            new_den = digits_to_num(new_den)

            if new_den != 0 and (numerator / denominator) == (new_num / new_den):
                return True

    return False

def solution_01():
    fractions = [(i, j) for i in range(10, 100) for j in range(i+1, 100)]
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
    return den_prod
    