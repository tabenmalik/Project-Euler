import itertools
from project_euler.misc import is_prime, sieve_of_eratosthenes_fast

SOLUTION = '-59231'

MAX_NUM = 1000

def consecutive_primes_of_quadratic(a, b):
    consec_primes = list()
    n = 0
    while True:
        f_n = (n * n) + (a * n) + b
        if not is_prime(f_n):
            break
        consec_primes.append(f_n)
        n += 1
    return consec_primes


def solution_01():
    coefficients = ((a, b) for a in range(-MAX_NUM+1, MAX_NUM) for b in range(-MAX_NUM, MAX_NUM+1))
    prime_lengths = {coeff_pair: len(consecutive_primes_of_quadratic(*coeff_pair)) for coeff_pair in coefficients}
    coeff_of_longest = max(prime_lengths, key=lambda x: prime_lengths[x])
    return coeff_of_longest[0] * coeff_of_longest[1] 


def solve():
    return str(solution_01())