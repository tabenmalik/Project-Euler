import itertools

from project_euler.misc import prime_seq

SOLUTION = '104743'

MAX_NUM = 10_001

def solution_01():
    primes_under_num = itertools.takewhile(lambda x: x[0] < MAX_NUM, enumerate(prime_seq()))
    _, primes_under_num = zip(*primes_under_num)
    return list(primes_under_num)[-1]


def solve():
    return str(solution_01())