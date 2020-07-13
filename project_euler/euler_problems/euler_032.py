import itertools
from pprint import pprint

from project_euler.misc import divisors, sieve_of_eratosthenes_fast

SOLUTION = '45228'

def expand_digits(num):
    return list(map(int, str(num)))


ALL_DIGITS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def is_pandigital(nums, through=9):
    if isinstance(nums, int):
        nums = [nums]

    digits_of_nums = map(expand_digits, nums)
    digits = list(itertools.chain(*digits_of_nums))
    
    return len(set(digits)) == len(digits) and len(digits) == through and 0 not in digits


def is_multidigital(nums):
    if isinstance(nums, int):
        nums = [nums]

    digits_of_nums = map(expand_digits, nums)
    digits = list(itertools.chain(*digits_of_nums))

    return len(set(digits)) != len(digits)

def solution_01():
    MAX_NUM = 1000000

    nums = range(4, MAX_NUM)
    primes = sieve_of_eratosthenes_fast(MAX_NUM)
    nums = set(nums).difference(primes)
    non_multidigital_nums = list(filter(lambda x: not is_multidigital(x), nums))
    
    
    divisors_of_nums = map(divisors, non_multidigital_nums)
    divisors_of_nums = map(lambda x: x[2:], divisors_of_nums)
    
    product_pairs = zip(non_multidigital_nums, divisors_of_nums)
    product_pairs = map(lambda x: list(zip(itertools.cycle([x[0]]), x[1][0::2], x[1][1::2])), product_pairs)
    product_pairs = itertools.chain(*product_pairs)
    product_pairs = filter(lambda x: sum(len(expand_digits(i)) for i in x) == 9, product_pairs)
   
    pan_digital_products = filter(is_pandigital, product_pairs)
    
    return sum(set(next(iter(zip(*pan_digital_products)))))


def solution_02():
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # digits = [1, 2, 3, 4]
    all_perms = list(itertools.permutations(digits))
    perms_columns = list(zip(*all_perms))
    
    products = set()
    for i in range(1, 5):
        for j in range(i+1, 6):
            a = zip(*perms_columns[0:i])
            b = zip(*perms_columns[i:j])
            product = zip(*perms_columns[j:])

            a = map(lambda x: list(map(str, x)), a)
            b = map(lambda x: list(map(str, x)), b)
            product = map(lambda x: list(map(str, x)), product)
            
            a = map(lambda x: ''.join(x), a)
            b = map(lambda x: ''.join(x), b)
            product = map(lambda x: ''.join(x), product)
            
            a = map(int, a)
            b = map(int, b)
            product = map(int, product)
            
            actual_products = filter(lambda trip: trip[0] == trip[1] * trip[2], zip(product, a, b))
            actual_products = list(zip(*actual_products))
            if len(actual_products) > 0:
                products.update(actual_products[0])

    return sum(products)


def solve():
    return str(solution_02())