import math

from project_euler.misc import prime_seq

SOLUTION = '142913828922'

MAX_NUM = 2_000_000


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


def solve():
    primes = sieve_of_eratosthenes_fast(MAX_NUM)

    return str(sum(primes))
