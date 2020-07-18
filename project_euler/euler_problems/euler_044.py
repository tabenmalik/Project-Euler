import math
import itertools

SOLUTION = '5482660'


def pentagonal(n):
    return (n * ((3 * n) - 1)) // 2


def is_pentagonal(p):
    if p <= 0:
        return False

    n1 = (0.5 + math.sqrt(0.25 + (6*p))) / 3
    n2 = (0.5 - math.sqrt(0.25 + (6*p))) / 3
    
    result = n1 > 0 and pentagonal(int(n1)) == p
    result |= n2 > 0 and pentagonal(int(n2)) == p

    return result

def pentagonal_seq(under=None):
    n = 1
    while True:
        yield pentagonal(n)
        n += 1
        if under is not None and n >= under:
            break


def solve():
    max_num = 10000
    for i in range(1, max_num):
        for j in range(i, max_num):
            pi = pentagonal(i)
            pj = pentagonal(j)
            
            p_sum = pi + pj
            p_diff = pj - pi

            if is_pentagonal(p_sum) and is_pentagonal(p_diff):
                return str(p_diff)

    