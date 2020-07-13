import math

from project_euler import misc

SOLUTION = '232792560'

MAX_NUM = 20

def is_divisible(i, divisor):
    while divisor > 1:
        if i % divisor != 0:
            return False
        divisor -= 1
    return True


def solution_01():
    num = (MAX_NUM - 1) * MAX_NUM
    while not is_divisible(num, MAX_NUM):
        num += (MAX_NUM - 1) * MAX_NUM

    return num


def solution_02():
    primes = list(misc.prime_seq(under=MAX_NUM+1))
    product = 1
    for prime in primes:
        exp = 1
        if prime * prime <= MAX_NUM:
            exp = int(math.log(MAX_NUM) // math.log(prime))
        product *= prime ** exp

    return product


def solve():
    return str(solution_02())