"""Functions for testing or manipulating properties of integers"""
from functools import reduce
import math
import operator


def concat(ints):
    """
    Combine several single digit numbers into a single number.

    Example:
    intjoin([1, 2, 3, 4, 5]) -> 12345
    """
    return int("".join(str(i) for i in ints))


def split(x):
    """ """
    return tuple(map(int, str(x)))


def ireversed(x):
    return int("".join(reversed(str(x))))


def palindromic(x):
    """
    Returns True if the number is a palindrome.
    A palidrome integer is an integer where the sequence of digits in reverse
    is equal the same integers.

    Examples:
        11211
        329923
    """
    return x == ireversed(x)


def sum_of_1_to_n(n):
    """
    Computes sum of all positive integers up to and including n
    """
    return (n * (n + 1)) // 2


def sum_of_a_to_n(a, n):
    """
    Computes sum of all positive integers from a to n, including a and n.
    """
    return sum_of_1_to_n(n) - sum_of_1_to_n(a - 1)


def sum_of_sqrs(num):
    """TODO: what does this do?
    TODO: reference"""
    return int((((2 * num) + 1) * (num + 1) * num) / 6)


def sum_of_cubes(num):
    """TODO: what does this do?
    TODO: reference"""
    return int(((num * num) * (num + 1) * (num + 1)) / 4)


def prime_factors_of_n(n, method="trial_division"):
    """Prime factors of n."""
    methods = {
        "trial_division": prime_factors_trial_division,
        "trial_division_naive": prime_factors_trial_division_naive,
    }

    return methods[method](n)


def prime_factors_trial_division_naive(num):
    """Prime factors of n using naive trial divison."""
    factor = 2

    while num > 1:
        if num % factor == 0:
            yield factor
            num //= factor
        else:
            factor += 1


def prime_factors_trial_division(num):
    """Prime factors of n using efficient trial division."""
    while num % 2 == 0:
        yield 2
        num //= 2

    factor = 3
    while factor * factor <= num:
        if num % factor == 0:
            yield factor
            num //= factor
        else:
            factor += 2

    if num != 1:
        yield num


def product(*args):
    """Returns the product of all arguments."""
    return reduce(operator.mul, args, 1)


def product_of_iter(iterable):
    """Returns the product of all elements in the iterable."""
    return product(*iterable)
