import math

from project_euler.misc import prime_seq

SOLUTION = '142913828922'

MAX_NUM = 2_000_000


def solution_01():
    ps = prime_seq(under=MAX_NUM)

    return sum(ps)


def sieve_of_eratosthenes_naive(under):
    bools = [False for i in range(0, under)]
    bools[0] = True
    bools[1] = True

    for i in range(4, under, 2):
        bools[i] = True

    for i in range(3, math.floor(math.sqrt(under))):
        if not bools[i]:
            for j in range(i*i, under, 2*i):
                bools[j] = True

    primes = [i for i, status in enumerate(bools) if not status]

    return primes

def solution_02():
    """
    Solution provided by Project Euler
    """
    primes = sieve_of_eratosthenes_naive(MAX_NUM)
    
    return sum(primes)


def sieve_of_eratosthenes_fast(under):
    sieve_len = int((under - 1) // 2) + 1 
    sieve = [False for i in range(0, sieve_len)]

    check_limit = (math.floor(math.sqrt(under)) - 1) // 2
    check_limit = int(check_limit) + 1

    for i in range(1, check_limit):
        if not sieve[i]:
            for j in range(2*i*(i+1), sieve_len, (2*i)+1):
                sieve[j] = True

    primes = [2]
    primes.extend([(2*i) + 1 for i in range(1, sieve_len) if not sieve[i]])

    return primes 


def solution_03():
    primes = sieve_of_eratosthenes_fast(MAX_NUM)

    return sum(primes)


def solve():
    return str(solution_03())