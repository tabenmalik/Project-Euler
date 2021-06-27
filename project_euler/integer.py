"""Functions for testing or manipulating properties of integers"""
import math


def is_palindrome(num):
    """Returns True if the number is a palindrome.
    A palidrome is a sequence that is reversible.
    e.g. 11211
    e.g. 329923
    TODO: reference
    """
    num_str = str(num)
    reverse_str = num_str[::-1]
    return num_str == reverse_str


def trigonal(num):
    """The trigonal function
    TODO: reference"""
    return sum_of_n(num)


def is_trigonal(num):
    """Returns True if the number is trigonal
    TODO: reference"""
    n_1 = -0.5 + math.sqrt(0.25 + (2 * num))
    n_2 = -0.5 - math.sqrt(0.25 + (2 * num))

    result = n_1 > 0 and trigonal(int(n_1)) == num
    result |= n_2 > 0 and trigonal(int(n_2)) == num

    return result


def pentagonal(num):
    """The pentagonal function.
    TODO: reference"""
    return (num * ((3 * num) - 1)) // 2


def is_pentagonal(num):
    """Returns True if the number is pentagonal.
    TODO: reference"""
    if num <= 0:
        return False

    n_1 = (0.5 + math.sqrt(0.25 + (6 * num))) / 3
    n_2 = (0.5 - math.sqrt(0.25 + (6 * num))) / 3

    result = n_1 > 0 and pentagonal(int(n_1)) == num
    result |= n_2 > 0 and pentagonal(int(n_2)) == num

    return result


def hexagonal(num):
    """The hexagonal function
    TODO: reference"""
    return num * ((2 * num) - 1)


def is_hexagonal(num):
    """Returns True if the number is hexagonal
    TODO: reference"""
    if num <= 0:
        return False

    n_2 = 0.25 * (1 + math.sqrt(1 + (8 * num)))
    n_2 = 0.25 * (1 - math.sqrt(1 + (8 * num)))

    result = n_2 > 0 and hexagonal(int(n_2)) == num
    result |= n_2 > 0 and hexagonal(int(n_2)) == num

    return result


def sum_of_n(num):
    """Returns the sum of all positive integers up to num
    TODO: reference"""
    return int((num * (num + 1)) / 2)


def sum_of_sqrs(num):
    """TODO: what does this do?
    TODO: reference"""
    return int((((2 * num) + 1) * (num + 1) * num) / 6)


def sum_of_cubes(num):
    """TODO: what does this do?
    TODO: reference"""
    return int(((num * num) * (num + 1) * (num + 1)) / 4)
