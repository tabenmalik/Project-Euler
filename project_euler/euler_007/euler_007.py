import itertools

from project_euler import primes

MAX_NUM = 10_001

def primes_it():
    yield 2
    i = 3
    while True:
        if primes.is_prime(i):
            yield i
        i += 2

def solution_01():
    i = MAX_NUM

    primes_under_num = itertools.takewhile(lambda x: x[0] < MAX_NUM, enumerate(primes_it()))
    _, primes_under_num = zip(*primes_under_num)
    return list(primes_under_num)[-1]