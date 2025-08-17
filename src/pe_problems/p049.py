import itertools

from pe.integer import concat, split
from pe.misc import sieve_of_eratosthenes_fast

SOLUTION = "296962999629"


def difference(l: list[int]) -> list[int]:
    d = []
    for i in range(1, len(l)):
        d.append(l[i - 1] - l[i])

    return d


def solve() -> str:
    primes = sieve_of_eratosthenes_fast(10000)
    primes = list(filter(lambda x: x >= 1000, primes))

    prime_pairs = [[p1, p2] for i, p1 in enumerate(primes) for p2 in primes[i + 1 :]]
    prime_pairs = filter(
        lambda x: sorted(split(x[0])) == sorted(split(x[1])), prime_pairs
    )
    prime_pairs = list(prime_pairs)

    chains = prime_pairs.copy()
    for prime_pair in prime_pairs:
        for i, chain in enumerate(chains):
            if prime_pair[0] == chain[-1] and set(difference(prime_pair)) == set(
                difference(chain)
            ):
                chains[i].append(prime_pair[1])

    chains = filter(lambda x: len(x) > 2, chains)
    chains = list(chains)

    result_nums = chains[1]
    result_nums = list(map(split, result_nums))
    result = [i for a in result_nums for i in a]
    return str(concat(result))
