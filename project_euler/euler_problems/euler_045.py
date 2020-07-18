from project_euler.integer import hexagonal
from project_euler.integer import is_pentagonal
from project_euler.integer import is_trigonal

SOLUTION = '1533776805'

def solve():
    n = 144
    while True:
        h = hexagonal(n)
        if is_pentagonal(h) and is_trigonal(h):
            return str(h)
        n += 1