from project_euler.misc import sum_of_n, prime_factors_trial_division, sieve_of_eratosthenes_fast
import math
from functools import reduce

SOLUTION = '76576500'

NUM_DIVISORS = 500


def triangle_num_seq():
    n = 1
    while True:
        yield sum_of_n(n)
        n += 1


def divisors_of_n(n):
    divisors = {1, n}
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            divisors.update([i, n / i])
            
    return divisors


def solution_01():
    triangle_nums = triangle_num_seq()

    for triangle_num in triangle_nums:
        divisors = list(divisors_of_n(triangle_num))
        if len(divisors) > NUM_DIVISORS:
            break
    
    return triangle_num


def prime_factors(n):
    primes = sieve_of_eratosthenes_fast(n)
    prime_divisors = list(filter(lambda x: n % x == 0, primes))

    exps = []
    for prime in prime_divisors:
        exp = 0
        while n % prime == 0:
            exp += 1
            n /= prime
        exps.append(exp)

    return prime_divisors, exps


def num_divisors_of_n(n):
    if n == 1:
        return 1
    
    primes, exps = prime_factors(n)
    num_divisors = reduce(lambda x, y: (x+1) * (y+1), exps)
    return num_divisors 

def solution_02():
    triangle_nums = triangle_num_seq()

    for triangle_num in triangle_nums:
        num_divisors = num_divisors_of_n(triangle_num)
        if num_divisors > NUM_DIVISORS:
            break
    
    return triangle_num


def solve():
    return str(solution_02())

