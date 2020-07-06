import numpy as np

from project_euler import misc

ANSWER = 6857

NUM = 600_851_475_143

def solution_01():
    prime_factors = reversed(list(misc.prime_factors_trial_division_naive(NUM)))
    return list(prime_factors)[0]


def solution_02():
    prime_factors = reversed(list(misc.prime_factors_trial_division(NUM)))
    return list(prime_factors)[0]


def solution_03():
    prime_factors = np.array(list(misc.prime_factors_trial_division(NUM)))
    return prime_factors.max()