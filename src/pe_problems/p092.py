import math
import functools
import itertools
from typing import Generator

from pe.integer import split

SOLUTION = "8581146"


def square(num: int) -> int:
    return num * num


def sum_of_square_digits(num: int) -> int:
    return sum(map(square, split(num)))


def sum_of_square_digits_seq(num: int) -> Generator[int, None, None]:
    yield num

    seen_1 = False
    seen_89 = False

    while True:
        if num == 1:
            if seen_1:
                break
            else:
                seen_1 = True
        elif num == 89:
            if seen_89:
                break
            else:
                seen_89 = True

        num = sum_of_square_digits(num)
        yield num


@functools.lru_cache
def sum_of_square_digits_ending(num: int) -> int:
    if num == 1 or num == 89:
        return num

    seq = sum_of_square_digits_seq(num)
    seq = iter(seq)
    _ = next(seq)
    return sum_of_square_digits_ending(next(seq))


def solve() -> str:
    count = 0

    for i in range(10_000_000, 1, -1):
        ending = sum_of_square_digits_ending(i)
        if ending == 89:
            count += 1

    return str(count)
