from __future__ import annotations

from collections.abc import Sequence
from itertools import permutations

from pe.integer import concat

SOLUTION = "16695334890"


def is_substring_divisible(digits: Sequence[int]) -> bool:
    if (
        digits[0] == 0
        or concat(digits[7:10]) % 17 != 0
        or concat(digits[6:9]) % 13 != 0
        or concat(digits[5:8]) % 11 != 0
        or concat(digits[4:7]) % 7 != 0
        or concat(digits[3:6]) % 5 != 0
        or concat(digits[2:5]) % 3 != 0
        or concat(digits[1:4]) % 2 != 0
    ):
        return False
    else:
        return True


def solve() -> str:
    special_nums = []
    for pandigital_number in permutations(list(range(10))):
        if is_substring_divisible(pandigital_number):
            special_nums.append(concat(pandigital_number))

    return str(sum(special_nums))
