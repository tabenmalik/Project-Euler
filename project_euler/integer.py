"""Functions for testing or manipulating properties of integers"""
import math


def is_palindrome(n):
    """
    Returns True if the number is a palindrome.
    A palidrome integer is an integer where the sequence of digits in reverse
    is equal the same integers.

    Examples:
        11211
        329923
    """
    num_str = str(n)
    reverse_str = num_str[::-1]
    return num_str == reverse_str


def trigonal(n):
    """
    Computes the nth trigonal number.
    A trigonal number is number of objects that can be arranged into an
    equilateral triangle.

    Examples:
        0, 1, 3, 6, 10, 15, ...
    """
    return math.comb(n + 1, 2)


def is_trigonal(n):
    """
    True if the number is trigonal
    See trigonal() for a definition of a trigonal number.
    """
    n_1 = -0.5 + math.sqrt(0.25 + (2 * n))
    n_2 = -0.5 - math.sqrt(0.25 + (2 * n))

    result = n_1 > 0 and trigonal(int(n_1)) == n
    result |= n_2 > 0 and trigonal(int(n_2)) == n

    return result


def pentagonal(n):
    """
    Computes the nth pentagonal number.
    Similar to a trigonal number, but instead is about the number for the outline
    of a pentagon, not the area.

    Examples:
        1, 5, 12, 22, 35, 51, ...
    """
    return (n * ((3 * n) - 1)) // 2


def is_pentagonal(n):
    """
    True if the number is pentagonal.
    See pentagonal() for a definition of a pentagonal number.
    """
    if n <= 0:
        return False

    n_1 = (0.5 + math.sqrt(0.25 + (6 * n))) / 3
    n_2 = (0.5 - math.sqrt(0.25 + (6 * n))) / 3

    result = n_1 > 0 and pentagonal(int(n_1)) == n
    result |= n_2 > 0 and pentagonal(int(n_2)) == n

    return result


def hexagonal(n):
    """
    Computes the n_th hexagonal number.
    Similar to a pentagonal number but for the shape of a hexagon.

    Examples:
        1, 6, 15, 28, 45, 66, ...
    """
    return n * ((2 * n) - 1)


def is_hexagonal(n):
    """
    True if the number is hexagonal.
    See hexagonal() for the definition of a hexagonal number.
    """
    if n <= 0:
        return False

    n_2 = 0.25 * (1 + math.sqrt(1 + (8 * n)))
    n_2 = 0.25 * (1 - math.sqrt(1 + (8 * n)))

    result = n_2 > 0 and hexagonal(int(n_2)) == n
    result |= n_2 > 0 and hexagonal(int(n_2)) == n

    return result


def sum_of_1_to_n(n):
    """
    Computes sum of all positive integers up to and including n
    """
    return (n * (n + 1)) // 2


def sum_of_a_to_n(a, n):
    """
    Computes sum of all positive integers from a to n, including a and n.
    """
    return sum_of_1_to_n(n) - sum_of_1_to_n(a-1)


def sum_of_sqrs(num):
    """TODO: what does this do?
    TODO: reference"""
    return int((((2 * num) + 1) * (num + 1) * num) / 6)


def sum_of_cubes(num):
    """TODO: what does this do?
    TODO: reference"""
    return int(((num * num) * (num + 1) * (num + 1)) / 4)


def prime_factors_of_n(n, method='trial_division'):
    """Prime factors of n."""
    methods = {
        'trial_division': prime_factors_trial_division,
        'trial_division_naive': prime_factors_trial_division_naive,
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
