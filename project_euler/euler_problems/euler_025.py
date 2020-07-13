from project_euler.misc import fibonacci_seq

SOLUTION = '4782'

MAX_DIGITS = 1_000

def solution_01():
    for i, fib in enumerate(fibonacci_seq(), start=1):
        if len(str(fib)) == MAX_DIGITS:
            break
    return i


def solve():
    return str(solution_01())