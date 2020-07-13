import operator
import math

import matplotlib.pyplot as plt

from project_euler.misc import num_to_digits, digits_to_num

SOLUTION = '40730'

def digit_factorial_sum(num):
    digits = num_to_digits(num)
    digit_factorials = map(math.factorial, digits)
    return sum(digit_factorials)


def solve():
    i = 2
    while True:
        digit_limit = i*math.factorial(9)
        num = digits_to_num(9 for _ in range(i))
        if digit_limit < num:
            break
        i += 1

    limit = digit_limit

    nums = list(range(10, limit))
    fact_sums = list(map(digit_factorial_sum, nums))
    equals = list(filter(lambda x: x[0] == x[1], zip(nums, fact_sums)))
    equals = next(iter(zip(*equals)))

    return str(sum(equals))
