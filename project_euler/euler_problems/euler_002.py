from functools import reduce
import operator

import numpy as np

from project_euler import misc

SOLUTION = '4613732'

MAX_NUM = 4_000_000

def solution_01():
    total = 2

    fib_1 = 1
    fib_2 = 2

    while fib_2 < MAX_NUM:
        fib_new = fib_2 + fib_1
        fib_1 = fib_2
        fib_2 = fib_new

        if fib_2 % 2 == 0:
            total += fib_2

    return total


def solution_02():
    fibs = misc.fibonacci_seq(MAX_NUM)
    even_fibs = filter(lambda x: x % 2 == 0, fibs)
    total = reduce(operator.add, even_fibs)

    return total


def solution_03():
    fibs = np.array(list(misc.fibonacci_seq(MAX_NUM)))
    even_fibs = fibs[fibs % 2 == 0]
    total = np.sum(even_fibs)

    return total


def solution_04():
    """
    Solution given by Project Euler
    """
    even_fibs = list(misc.even_fibonacci_seq(MAX_NUM))
    total = sum(even_fibs)

    return total


def solve():
    return str(solution_04())