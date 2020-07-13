import itertools
from functools import reduce
import operator

SOLUTION = '31875000'


def solve():
    SUM_NUM = 1000

    triplets = ((i, j, SUM_NUM-i-j) for i in range(1, SUM_NUM) 
                for j in range(i+1, SUM_NUM-i))

    triplets = filter(lambda t: t[0]**2 + t[1]**2 == t[2]**2, triplets)
    triplets = list(triplets)
    
    assert(len(triplets) == 1)
    prod = reduce(operator.mul, triplets[0])
    return str(prod)
