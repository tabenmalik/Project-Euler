import itertools
from collections.abc import Generator
from typing import ParamSpec
from typing import TypeVar
from collections.abc import Sequence
from collections.abc import Callable
from typing import Any
from collections.abc import Iterable
from pe.integer import split, concat
from pe.misc import divisors
from pe.misc import sieve_of_eratosthenes_fast

SOLUTION = "26033"


def prime_seq() -> Generator[int, None, None]:
    """
    A generator of prime numbers
    """
    yield 2

    i = 3
    while True:
        if is_prime(i):
            yield i
        i += 2


def num_splits(num: int) -> Generator[tuple[int, int], None, None]:
    digits = split(num)
    for i in range(1, len(digits)):
        yield concat(digits[:i]), concat(digits[i:])


def concat_nums(nums: Iterable[int]) -> int:
    return int("".join(map(str, nums)))


P = ParamSpec("P")
R = TypeVar("R")


def memoize(func: Callable[P, R]) -> Callable[P, R]:
    results: dict[Any, R] = {}

    def _memoized_func(*args: P.args, **kwargs: P.kwargs) -> R:
        if args in results:
            return results[args]

        result = func(*args, **kwargs)
        results[args] = result
        return result

    return _memoized_func


PRIME_CACHE = set(sieve_of_eratosthenes_fast(100_000_000))
MAX_CACHED_PRIME = max(PRIME_CACHE)


@memoize
def is_prime(num: int) -> bool:
    if num <= MAX_CACHED_PRIME:
        return num in PRIME_CACHE
    return num != 1 and len(divisors(num)) == 2


@memoize
def is_prime_pair(primes_set: Iterable[int]) -> bool:
    primes_list = list(primes_set)
    concat_num = concat_nums(primes_list)
    reverse_concat_num = concat_nums(reversed(primes_list))
    return is_prime(concat_num) and is_prime(reverse_concat_num)


def expands_prime_pair_set(prime_set: Sequence[int], new_prime: int) -> bool:
    for num in prime_set:
        if not is_prime_pair(frozenset([num, new_prime])):
            return False

    return True


def solve() -> str:
    prime_pair_sets: set[Any] = set()

    for prime in prime_seq():
        new_sets = [frozenset([prime])]
        for prime_pair_set in prime_pair_sets:
            if expands_prime_pair_set(prime_pair_set, prime):
                expanded_pair_set = prime_pair_set | frozenset([prime])
                if len(expanded_pair_set) == 5:
                    return str(sum(expanded_pair_set))
                new_sets.append(expanded_pair_set)
        prime_pair_sets.update(new_sets)

    return ""
