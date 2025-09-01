from functools import reduce
import operator
from typing import cast

from pe.integer import split

SOLUTION = "210"


def champernowne_digit(n: int) -> int:
    level = 0
    level_num_digits = 0

    while n > level_num_digits:
        level += 1
        level_num_digits += 9 * (10 ** (level - 1)) * level

    last_level_num_digits = cast(int, level_num_digits - (9 * (10 ** (level - 1)) * level))
    digits_into_level = n - last_level_num_digits

    sub_level = (digits_into_level - 1) // level

    sub_level_num = (10 ** (level - 1)) + sub_level

    digits = split(sub_level_num)
    digit = digits[(digits_into_level - 1) % level]
    return digit


def solve() -> str:
    exponents = [0, 1, 2, 3, 4, 5, 6]
    nth_digits = map(lambda x: 10**x, exponents)
    digits = map(champernowne_digit, nth_digits)
    prod = reduce(operator.mul, digits)

    return str(prod)
