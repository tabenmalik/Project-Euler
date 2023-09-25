"""
Odd Period Square Roots
"""

from math import floor, isqrt, sqrt, gcd


def root_continued_fraction(n):
    b = 1
    c = 0
    d = 1
    a0 = isqrt(n)
    a = a0

    if a0 * a0 == n:
        return a0, []

    first_triplet = tuple()
    coeffs = list()

    while True:
        b, c, d = (
            d * b,
            d * ((d * a) - c),
            (b * b * n) - (c * c) + (a * d) * ((2 * c) - (a * d)),
        )

        g = gcd(b, c, d)

        b, c, d = (b // g, c // g, d // g)

        a = floor((floor(b * sqrt(n)) + c) / d)

        if not first_triplet:
            first_triplet = (b, c, d)
        elif (b, c, d) == first_triplet:
            break

        coeffs.append(a)

    return a0, tuple(coeffs)


def solve():
    """ """
    N = 10_000
    odd_periods = 0
    for n in range(2, N + 1):
        period = len(root_continued_fraction(n)[1])
        odd_periods += period % 2

    return str(odd_periods)
