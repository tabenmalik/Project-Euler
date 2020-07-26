import itertools
import operator

from project_euler.integer import is_palindrome

SOLUTION = '906609'

NUM_DIGITS = 3


def solve():
    num_low = 10 ** (NUM_DIGITS - 1)
    num_high = 10 ** NUM_DIGITS
    a = list(range(num_low, num_high))
    b = a.copy()

    pairs = itertools.product(a, b)
    products = map(lambda x: operator.mul(*x), pairs)
    products = set(products)
    palindromes = filter(is_palindrome, products)
    largest_palindrome = max(palindromes)
    
    return str(largest_palindrome)
