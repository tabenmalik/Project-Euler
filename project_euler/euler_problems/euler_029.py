SOLUTION = 9183

MAX_NUM = 100


def solution_01():
    powers = set(a**b for a in range(2, MAX_NUM+1) for b in range(2, MAX_NUM+1))
    return len(powers)