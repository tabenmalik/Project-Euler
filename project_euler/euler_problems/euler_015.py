from functools import reduce
import operator
import math



GRID_SIZE = 20


def solve():
    terms = map(lambda i: (GRID_SIZE + i) / i, range(1, GRID_SIZE+1))
    prod = reduce(operator.mul, terms)

    return str(math.ceil(prod))
