import math
from functools import lru_cache

SOLUTION = ''

@lru_cache
def proper_divisors(n):
    if n == 1:
        return []

    divisors = []
    divisors.append(1)
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    return sorted(divisors)


def divisor_chain(n):
    chain = list()
    a = n
    while a not in chain:
        chain.append(a)
        a = sum(proper_divisors(a))
        if a > 1_000_000:
            chain = []
            break
    if a == n:
        chain.append(n)
    return chain


def solve():
    longest_chain = []
    for i in range(1_000_000):
        chain = divisor_chain(i)
        if not chain or chain[-1] != chain[0]:
            continue
        if len(chain) > len(longest_chain):
            longest_chain = chain

    return str(min(longest_chain))

