import math

from pe.misc import is_prime
from pe.misc import sieve_of_eratosthenes_fast

SOLUTION = "5777"

def is_goldbach_composite(n):
    primes = sieve_of_eratosthenes_fast(under=n)

    for prime in primes:
        a = (n - prime) / 2
        b = math.sqrt(a)

        if int(b) ** 2 == a:
            return True


def solve():
    i = 35
    while True:
        if not is_prime(i) and not is_goldbach_composite(i):
            return str(i)

        i += 2
