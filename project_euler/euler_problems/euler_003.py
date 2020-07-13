import numpy as np

from project_euler import misc

SOLUTION = '6857'

NUM = 600_851_475_143


def solve():
    prime_factors = misc.prime_factors_trial_division(NUM)
    return str(max(prime_factors))
