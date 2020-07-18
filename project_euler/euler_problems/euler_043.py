from project_euler.sequences import permutations_seq
from project_euler.misc import digits_to_num, num_to_digits

SOLUTION = '16695334890'

PRIMES = (2, 3, 5, 7, 11, 13, 17)


def is_substring_divisible(digits):
    groups = (digits[i:i+3] for i in range(1, len(digits)-2))
    group_nums = map(digits_to_num, groups)

    for num, prime in zip(group_nums, PRIMES):
        if num % prime != 0:
            return False

    return True


def solve():
    pandigital_numbers = permutations_seq([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    pandigital_numbers = filter(lambda x: x[0] != 0, pandigital_numbers)
    special_nums = filter(is_substring_divisible, pandigital_numbers)
    special_nums = map(digits_to_num, special_nums)
    return str(sum(special_nums))