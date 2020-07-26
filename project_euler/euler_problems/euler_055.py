from project_euler.misc import num_to_digits, digits_to_num
from project_euler.integer import is_palindrome

SOLUTION = '249'


def is_lychrel(n, iterations=50):
    num = n
    for _ in range(0, iterations):
        reversed_num = digits_to_num(reversed(num_to_digits(num)))
        num += reversed_num
        if is_palindrome(num):
            return False
    
    return True

def solve():
    lychrel_nums = list(filter(is_lychrel, range(1, 10_000)))
    return str(len(lychrel_nums))