import math

from project_euler.sequences import prime_seq

SOLUTION = '232792560'

MAX_NUM = 20

def solve():
    primes = list(prime_seq(under=MAX_NUM+1))
    product = 1
    for prime in primes:
        exp = 1
        if prime * prime <= MAX_NUM:
            exp = int(math.log(MAX_NUM) // math.log(prime))
        product *= prime ** exp

    return str(product)
