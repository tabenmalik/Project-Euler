SOLUTION = '9183'

MAX_NUM = 100


def solve():
    powers = set(a**b for a in range(2, MAX_NUM+1) for b in range(2, MAX_NUM+1))
    return str(len(powers))
