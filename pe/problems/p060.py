"""
Prime Pair Sets
"""

import itertools
from pe.integer import split, concat
from pe.misc import divisors
from pe.misc import sieve_of_eratosthenes_fast


def prime_seq():
    """
    A generator of prime numbers
    """
    yield 2

    i = 3
    while True:
        if is_prime(i):
            yield i
        i += 2


def num_splits(num):
    digits = split(num)
    for i in range(1, len(digits)):
        yield concat(digits[:i]), concat(digits[i:])


def concat_nums(nums):
    return int("".join(map(str, nums)))


def memoize(func):
    results = {}

    def _memoized_func(*args):
        if args in results:
            return results[args]

        result = func(*args)
        results[args] = result
        return result

    return _memoized_func


PRIME_CACHE = set(sieve_of_eratosthenes_fast(100_000_000))
MAX_CACHED_PRIME = max(PRIME_CACHE)


@memoize
def is_prime(num):
    if num <= MAX_CACHED_PRIME:
        return num in PRIME_CACHE
    return num != 1 and len(divisors(num)) == 2


@memoize
def is_prime_pair(primes_set):
    primes_list = list(primes_set)
    concat_num = concat_nums(primes_list)
    reverse_concat_num = concat_nums(reversed(primes_list))
    return is_prime(concat_num) and is_prime(reverse_concat_num)


def expands_prime_pair_set(prime_set, new_prime):
    for num in prime_set:
        if not is_prime_pair(frozenset([num, new_prime])):
            return False

    return True


def solve():
    prime_pair_sets = set()

    for prime in prime_seq():
        new_sets = [frozenset([prime])]
        for prime_pair_set in prime_pair_sets:
            if expands_prime_pair_set(prime_pair_set, prime):
                expanded_pair_set = prime_pair_set | frozenset([prime])
                if len(expanded_pair_set) == 5:
                    return str(sum(expanded_pair_set))
                new_sets.append(expanded_pair_set)
        prime_pair_sets.update(new_sets)
