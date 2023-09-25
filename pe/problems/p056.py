"""
Powerful Digit Sum
"""

from pe.integer import split


def solve():
    nums = [x**y for x in range(0, 100) for y in range(0, 100)]

    nums = map(split, nums)
    digit_sums = map(sum, nums)

    return str(max(digit_sums))
