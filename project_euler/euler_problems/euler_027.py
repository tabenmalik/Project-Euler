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


def solve():
    a = range(-MAX_NUM+1, MAX_NUM)
    b = range(-MAX_NUM, MAX_NUM+1)
    coeff_pairs = list(itertools.product(a, b))

    quadratic_primes = list(itertools.starmap(consecutive_primes_of_quadratic, coeff_pairs))
    lengths = map(len, quadratic_primes)
    coeff_lengths = {coeff_pair:length for coeff_pair, length in zip(coeff_pairs, lengths)}

    coeff_of_longest = max(coeff_lengths, key=lambda x: coeff_lengths[x])
    return str(coeff_of_longest[0] * coeff_of_longest[1])
