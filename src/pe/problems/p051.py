import itertools

from pe.integer import split
from pe.sequences import prime_seq
from pe.sequences import permutations_seq
from pe.misc import is_prime


def digit_replacements(num, digit):
    num_str = str(num)
    digit_str = str(digit)
    results = map(
        lambda i: num_str.replace(digit_str, i),
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    )
    results = map(int, results)
    num_factor_lower = 10 ** (len(num_str) - 1)
    results = filter(lambda x: x >= num_factor_lower, results)
    return list(results)


def solve():
    for prime in prime_seq():
        for digit in set(split(prime)):
            replacement_nums = digit_replacements(prime, digit)
            replacement_nums = list(filter(is_prime, replacement_nums))
            if len(replacement_nums) == 8:
                return str(replacement_nums[0])
