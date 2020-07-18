from project_euler.sequences import even_fibonacci_seq

SOLUTION = '4613732'

MAX_NUM = 4_000_000

def solve():
    """
    Solution given by Project Euler
    """
    even_fibs = list(even_fibonacci_seq(MAX_NUM))
    total = sum(even_fibs)

    return str(total)
