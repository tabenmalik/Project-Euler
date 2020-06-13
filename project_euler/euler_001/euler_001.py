from functools import reduce
import operator

import numpy as np

MAX_NUM=1000

def solution_01():
    total = 0
    for i in range(0, MAX_NUM):
        if i % 5 == 0 or i % 3 == 0:
            total += i

    return total


def solution_02():
    nums = range(0, MAX_NUM)
    multiples_func = lambda x: x % 5 == 0 or x % 3 == 0
    total = reduce(operator.add, filter(multiples_func, nums))

    return total


def solution_03():
    num_3s = np.arange(0, MAX_NUM, 3)
    num_5s = np.arange(0, MAX_NUM, 5)
    num_15s = np.arange(0, MAX_NUM, 15)

    total = np.sum(num_3s) + np.sum(num_5s) - np.sum(num_15s)

    return total