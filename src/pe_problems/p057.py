from functools import reduce
import operator
from typing import ParamSpec
from typing import TypeVar
from typing import Callable
from typing import Any

from pe.integer import split

SOLUTION = "153"

P = ParamSpec("P")
R = TypeVar("R")


def memoize(func: Callable[P, R]) -> Callable[P, R]:
    results: dict[Any, R] = {}

    def _memoized_func(*args: P.args, **kwargs: P.kwargs) -> R:
        if args in results:
            return results[args]

        result = func(*args, **kwargs)
        results[args] = result
        return result

    return _memoized_func


@memoize
def prime_factors(num: int) -> list[int]:
    factor = 2

    while factor * factor <= num:
        if num % factor == 0:
            return [factor] + prime_factors(num // factor)
        else:
            factor += 1

    return [1, num]


def reduce_fraction(frac: tuple[int, int]) -> tuple[int, int]:
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


def add_fractions(
    f1: int | tuple[int, int], f2: int | tuple[int, int]
) -> tuple[int, int]:
    if isinstance(f1, int):
        f1 = (f1, 1)

    if isinstance(f2, int):
        f2 = (f2, 1)

    return (f1[0] * f2[1] + f2[0] * f1[1], f1[1] * f2[1])


@memoize
def expand_root_2_fractional(iterations: int) -> tuple[int, int]:
    if iterations == 1:
        return (1, 2)

    result = add_fractions(2, expand_root_2_fractional(iterations - 1))
    result = result[1], result[0]
    return result


def expand_root_2(iterations: int) -> tuple[int, int]:
    return add_fractions(1, expand_root_2_fractional(iterations))


def solve() -> str:
    expanded_fracs = map(expand_root_2, range(1, 1_001))
    frac_digits = map(lambda frac: (split(frac[0]), split(frac[1])), expanded_fracs)
    frac_digits = map(lambda frac: (len(frac[0]), len(frac[1])), frac_digits)
    frac_digits = filter(lambda frac: frac[0] > frac[1], frac_digits)

    return str(len(list(frac_digits)))
