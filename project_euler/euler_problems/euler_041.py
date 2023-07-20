from project_euler.integer import concat
from project_euler.sequences import permutations_seq
from project_euler.misc import prime_factors

SOLUTION = '7652413'

def is_prime(n):
    if len(list(prime_factors(n))) == 1:
        return True

    return False


def solve():

    pandigital_numbers = permutations_seq([1, 2, 3, 4, 5, 6, 7])
    pandigital_numbers = reversed(list(pandigital_numbers))
    pandigital_numbers = map(concat, pandigital_numbers)
    
    pandigital_numbers = filter(lambda x: x % 2 != 0, pandigital_numbers)
    pandigital_numbers = filter(lambda x: x % 3 != 0, pandigital_numbers)
    pandigital_numbers = filter(lambda x: x % 5 != 0, pandigital_numbers)
    pandigital_numbers = filter(lambda x: x % 7 != 0, pandigital_numbers)

    for pandigital_number in pandigital_numbers:
        if is_prime(pandigital_number):
            return str(pandigital_number)
    
