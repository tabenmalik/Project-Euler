from functools import reduce
import operator

from pe.integer import split


def champernowne_digit(n):
    level = 0
    level_num_digits = 0

    while n > level_num_digits:
        level += 1
        level_num_digits += 9 * (10 ** (level - 1)) * level

    last_level_num_digits = level_num_digits - (9 * (10 ** (level - 1)) * level)
    digits_into_level = n - last_level_num_digits

    sub_level = (digits_into_level - 1) // level

    sub_level_num = (10 ** (level - 1)) + sub_level
    return split(sub_level_num)[(digits_into_level - 1) % level]


def solve():
    exponents = [0, 1, 2, 3, 4, 5, 6]
    nth_digits = map(lambda x: 10**x, exponents)
    digits = map(champernowne_digit, nth_digits)
    prod = reduce(operator.mul, digits)

    return str(prod)
