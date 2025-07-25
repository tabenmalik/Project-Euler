from pe.integer import split, concat
from pe.misc import sieve_of_eratosthenes_fast, is_prime

SOLUTION = "55"


def cycle_digits(num):
    yield num

    digits = list(split(num))
    digits = digits[1:] + digits[:1]
    new_num = concat(digits)
    while new_num != num:
        yield new_num
        digits = digits[1:] + digits[:1]
        new_num = concat(digits)


def solve():
    limit = 1_000_000
    primes = set(sieve_of_eratosthenes_fast(limit))

    num_cycles = map(lambda x: (x, set(cycle_digits(x))), primes)
    prime_cycles = filter(lambda x: x[1].issubset(primes), num_cycles)
    return str(len(list(prime_cycles)))
