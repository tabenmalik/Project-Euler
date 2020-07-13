from functools import reduce
import operator
import math

SOLUTION = '137846528820'

GRID_SIZE = 20

GRAPH_CACHE = {}
def grid_paths(x, y):
    if x == 0 or y == 0:
        return 1

    if (x, y) in GRAPH_CACHE:
        return GRAPH_CACHE[(x, y)]
    
    paths = grid_paths(x-1, y) + grid_paths(x, y-1)
    GRAPH_CACHE[(x, y)] = paths
    return paths

def solution_01():
    """
    Brute force
    """

    count = grid_paths(GRID_SIZE, GRID_SIZE)

    return count


def solution_02():
    terms = map(lambda i: (GRID_SIZE + i) / i, range(1, GRID_SIZE+1))
    prod = reduce(operator.mul, terms)

    return math.ceil(prod)


def solve():
    return str(solution_02())