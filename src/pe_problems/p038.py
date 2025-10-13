from itertools import permutations
from collections.abc import Sequence
from pe.integer import concat, split

SOLUTION = "932718654"


def contains_multiples(num: int, digits: Sequence[int]) -> bool:
    multiplier = 1

    while len(digits) > 0:
        multiple = num * multiplier
        multiple_digits = split(multiple)

        sub_digits = digits[: len(multiple_digits)]
        if multiple_digits != sub_digits:
            return False

        digits = digits[len(multiple_digits) :]
        multiplier += 1

    return True


def solve() -> str:
    pandigitals = reversed(list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9])))

    for pandigital in pandigitals:
        for i in range(1, 5):
            if contains_multiples(concat(pandigital[:i]), pandigital):
                return str(concat(pandigital))

    return ""
