"""
"""

SOLUTION = ''

from math import floor, isqrt, sqrt, gcd

def e_continued_fraction_coeffs(n):
    if n == 0:
        return

    yield 2
    
    if n == 1:
        return

    n -= 1 
    
    for k in range(n // 3):
        yield 1
        yield 2 * (k + 1)
        yield 1

    print(n)

    if (n - 1) % 3 == 0:
        yield 1
    elif (n - 1) % 3 == 1:
        yield 1
        yield 2 * ((n // 3) + 1)
    else:
        yield 1
        yield 2 * ((n // 3) + 1)
        yield 1


def solve():
    """
    """
    pass
