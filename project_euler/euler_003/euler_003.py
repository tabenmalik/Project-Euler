import numpy as np

NUM = 600_851_475_143


def trial_division_naive(num):
    factor = 2

    while num > 1:
        if num % factor == 0:
            yield factor
            num //= factor
        else:
            factor += 1


def trial_division(num):
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

def solution_01():
    prime_factors = reversed(list(trial_division_naive(NUM)))
    return list(prime_factors)[0]


def solution_02():
    prime_factors = reversed(list(trial_division(NUM)))
    return list(prime_factors)[0]


def solution_03():
    prime_factors = np.array(list(trial_division(NUM)))
    return prime_factors.max()