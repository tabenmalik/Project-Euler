from math import isqrt
from pe.integer import split
from functools import reduce
from operator import mul
from collections import defaultdict
from collections import Counter

SOLUTION = "8319823"


def solve() -> str:
    min_ratio = 10_000_000.0
    min_n = 0
    prime_divisors = defaultdict(set)
    max_n = 10_000_000
    for i in range(4, max_n, 2):
        prime_divisors[i].add(2)
    for i in range(3, max_n):
        if len(prime_divisors[i]) == 0:
            for j in range(i * 2, max_n, i):
                prime_divisors[j].add(i)

    for i in range(1, max_n):
        numerator = reduce(mul, prime_divisors[i], 1)
        denominator = reduce(mul, ((p - 1) for p in prime_divisors[i]), 1)
        numerator, denominator = i, denominator * (i // numerator)
        if numerator != denominator and Counter(split(numerator)) == Counter(split(denominator)):
            ratio = numerator / denominator
            if ratio < min_ratio:
                min_ratio = ratio
                min_n = i
    return str(min_n)


if __name__ == "__main__":
    SystemExit(solve() == SOLUTION)
