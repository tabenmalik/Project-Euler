from __future__ import annotations

import math
from collections import Counter
from collections.abc import Iterator
from fractions import Fraction
from itertools import starmap
from typing import NamedTuple

from pe.integer import concat
from pe.integer import split

SOLUTION = "100"


class Rational(NamedTuple):
    numerator: int
    denominator: int

    def as_fraction(self) -> Fraction:
        return Fraction(self.numerator, self.denominator)

    def equivalent(self, other: Rational) -> bool:
        return self.as_fraction() == other.as_fraction()


def rationals() -> Iterator[Rational]:
    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):
            yield Rational(numerator, denominator)


def trivial(rational: Rational) -> bool:
    return (
        rational.numerator % 10 == 0
        and rational.denominator % 10 == 0
    )


def cancel(rational: Rational) -> Rational:
    numerator_digits = list(split(rational.numerator))
    denominator_digits = list(split(rational.denominator))

    numerator_digit_count = Counter(numerator_digits)
    denominator_digit_count = Counter(denominator_digits)
    common_digit_counts = numerator_digit_count & denominator_digit_count

    for digit, count in common_digit_counts.items():
        for _ in range(count):
            numerator_digits.remove(digit)
            denominator_digits.remove(digit)

    if not denominator_digits or denominator_digits[0] == 0:
        return rational

    return Rational(concat(numerator_digits), concat(denominator_digits))


def solve() -> str:
    special_rationals = []
    for rational in rationals():
        if not trivial(rational):
            cancelled_rational = cancel(rational)
            if (
                rational != cancelled_rational
                and rational.equivalent(cancelled_rational)
            ):
                special_rationals.append(rational)

    special_fractions = tuple(starmap(Fraction, special_rationals))
    product = math.prod(special_fractions)
    return str(product.denominator)
