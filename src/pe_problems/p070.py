from math import isqrt
from pe.integer import split
from functools import reduce
from operator import mul
from collections import defaultdict
from collections import Counter
from pe.misc import sieve_of_eratosthenes_fast
from typing import Sequence

SOLUTION = "8319823"


def totient_seq(limit: int) -> Sequence[int]:
    totients = [0] * limit
    primes = sieve_of_eratosthenes_fast(limit)

    totients[0] = 0
    totients[1] = 1
    totients[2] = 1

    for n in range(1, limit // 2):
        for prime in primes:
            if n * prime >= limit:
                break
            totients[n * prime] = totients[n] * (prime if n % prime == 0 else prime - 1)

    return totients


def solve() -> str:
    min_ratio = 10_000_000.0
    min_n = 0
    totients = totient_seq(10_000_000)
    for n, totient_n in enumerate(totients[2:], 2):
        if sorted(str(n)) == sorted(str(totient_n)):
            ratio = n / totient_n
            if ratio < min_ratio:
                min_ratio = ratio
                min_n = n
    return str(min_n)


if __name__ == "__main__":
    SystemExit(solve() == SOLUTION)
