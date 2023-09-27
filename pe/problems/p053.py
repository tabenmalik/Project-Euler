"""
Combinatoric Selections

.. raw:: html
   :url: https://projecteuler.net/minimal=053
"""

import math


def choose(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def solve():
    count = 0
    for n in range(1, 101):
        for r in range(0, n + 1):
            num = choose(n, r)
            if num > 1_000_000:
                count += 1

    return str(count)
