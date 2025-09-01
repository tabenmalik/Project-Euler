from itertools import takewhile, combinations, groupby
from typing import Generator
from typing import Iterable
from typing import Any

from pe.integer import split

SOLUTION = "127035954683"


def positive_integers_seq(start: int = 1, step: int = 1) -> Generator[int, None, None]:
    n = start

    while True:
        yield n
        n += step


def cube(n: int) -> int:
    return n**3


def solve() -> str:
    num_digits = 1

    while True:
        start = 10 ** (num_digits - 1)
        start = int(start ** (1 / 3)) + 1

        nums = positive_integers_seq(start=start)
        nums = map(cube, nums)
        nums = takewhile(lambda x: len(split(x)) == num_digits, nums)
        nums = list(nums)

        digit_sets = map(split, nums)
        digit_sets = map(sorted, digit_sets)
        digit_sets = map(tuple, digit_sets)

        digit_set_to_nums: dict[tuple[int, ...], list[int]] = {}

        for digit_set, num in zip(digit_sets, nums):
            if digit_set in digit_set_to_nums:
                digit_set_to_nums[digit_set].append(num)
            else:
                digit_set_to_nums[digit_set] = [num]

            if len(digit_set_to_nums[digit_set]) == 5:
                return str(min(digit_set_to_nums[digit_set]))

        num_digits += 1
