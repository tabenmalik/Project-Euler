from math import isqrt
from itertools import count, takewhile, islice

from project_euler.predicates import le

def squares(start=1):
    for i in count(start):
        yield i**2

def nonsquares():
    for i in count(2):
        if isqrt(i)**2 != i:
            yield i

def diophantine_min_x(D):
    for m in squares():
        print("m:", m)
        d = m * D + 1
        if isqrt(d)**2 == d:
            return isqrt(d)

def solve():
    maxx = 3
    maxD = 2

    for D in takewhile(le(1000), nonsquares()):
        x = diophantine_min_x(D)
        print(D, x)
        if x > maxx:
            maxx = x
            maxD = D

    return str(maxD)
