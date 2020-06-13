from functools import reduce
import operator

import numpy as np

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


def fibonacci(end=None):
    fib_1 = 1
    fib_2 = 2

    yield fib_1
    yield fib_2

    while end is None or fib_2 < end:
        fib_new = fib_2 + fib_1
        
        yield fib_new
        
        fib_1 = fib_2
        fib_2 = fib_new 

def solution_02():
    fibs = fibonacci(MAX_NUM)
    even_fibs = filter(lambda x: x % 2 == 0, fibs)
    total = reduce(operator.add, even_fibs)

    return total


def solution_03():
    fibs = np.array(list(fibonacci(MAX_NUM)))
    even_fibs = fibs[fibs % 2 == 0]
    total = np.sum(even_fibs)

    return total