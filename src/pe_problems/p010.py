"""Project Euler problem 010: https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math

SOLUTION = "142913828922"

MAX_NUM = 2_000_000


def sieve_of_eratosthenes_fast(under):
    """Returns a list primes.

    Uses the Sieve of Eratosthenes methodology for determining all
    prime numbers under a limit.

    Args:
        under (int): find the primes below this number

    Returns:
        list(int): prime numbers
    """
    sieve_len = int((under - 1) // 2) + 1
    sieve = [False for i in range(0, sieve_len)]

    check_limit = (math.floor(math.sqrt(under)) - 1) // 2
    check_limit = int(check_limit) + 1

    for i in range(1, check_limit):
        if not sieve[i]:
            for j in range(2 * i * (i + 1), sieve_len, (2 * i) + 1):
                sieve[j] = True

    primes = [2]
    primes.extend([(2 * i) + 1 for i in range(1, sieve_len) if not sieve[i]])

    return primes


def solve():
    """Solves Project Euler problem 010"""
    primes = sieve_of_eratosthenes_fast(MAX_NUM)
    return str(sum(primes))
