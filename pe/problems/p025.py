from pe.sequences import fibonacci_seq


MAX_DIGITS = 1_000


def solve():
    for i, fib in enumerate(fibonacci_seq(), start=1):
        if len(str(fib)) == MAX_DIGITS:
            break
    return str(i)
