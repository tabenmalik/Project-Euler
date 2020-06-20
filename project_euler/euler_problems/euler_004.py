import itertools
import logging
import operator

LOGGER = logging.getLogger(__name__)

ANSWER = 906609

NUM_DIGITS = 3


def is_palindrome(num):
    num_str = str(num)
    reverse_str = num_str[::-1]
    return num_str == reverse_str


def solution_01():
    max_num = 10 ** NUM_DIGITS
    largest_palindrome = 0
    
    a = 10 ** (NUM_DIGITS - 1)
    while a < max_num:
        b = b = 10 ** (NUM_DIGITS - 1) 
        while b < max_num:
            product = a * b
            LOGGER.trace('a: {:d}, b: {:d}, prod: {:d}'.format(a, b, product))
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
                LOGGER.debug('Found new largest palindrome: {:d}'.format(product))
            
            b += 1
        a += 1

    return largest_palindrome


def solution_02():
    num_low = 10 ** (NUM_DIGITS - 1)
    num_high = 10 ** NUM_DIGITS
    a = list(range(num_low, num_high))
    b = a.copy()

    pairs = itertools.product(a, b)
    products = map(lambda x: operator.mul(*x), pairs)
    palindromes = filter(is_palindrome, products)
    largest_palindrome = max(palindromes)
    
    return largest_palindrome


def solution_03():
    """
    Just like solution 02 but removes duplicate
    products before testing palindromes
    """
    num_low = 10 ** (NUM_DIGITS - 1)
    num_high = 10 ** NUM_DIGITS
    a = list(range(num_low, num_high))
    b = a.copy()

    pairs = itertools.product(a, b)
    products = map(lambda x: operator.mul(*x), pairs)
    products = set(products)
    palindromes = filter(is_palindrome, products)
    largest_palindrome = max(palindromes)
    
    return largest_palindrome
