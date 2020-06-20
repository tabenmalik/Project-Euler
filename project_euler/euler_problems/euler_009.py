import itertools
from functools import reduce
import operator

ANSWER = 31875000


def solution_01():
    SUM_NUM = 1000

    nums = range(SUM_NUM)
    triplets = ((i, j, SUM_NUM-i-j) for i in range(1, SUM_NUM) 
                for j in range(i+1, SUM_NUM-i))

    triplets = filter(lambda t: t[0]**2 + t[1]**2 == t[2]**2, triplets)
    triplets = list(triplets)
    
    assert(len(triplets) == 1)
    prod = reduce(operator.mul, triplets[0])
    return prod