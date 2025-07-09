"""
Project Euler problem 004: https://projecteuler.net/problem=4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import itertools
from operator import mul

from pe.integer import palindromic


SOLUTION = "906609"


def solve():
    """Solves Project Euler problem 004"""
    NUM_DIGITS = 3
    start = 10 ** (NUM_DIGITS - 1)
    stop = 10**NUM_DIGITS
    pairs = itertools.combinations(range(start, stop), 2)
    products = itertools.starmap(mul, pairs)
    palindromes = filter(palindromic, products)
    largest_palindrome = max(palindromes)

    return str(largest_palindrome)
