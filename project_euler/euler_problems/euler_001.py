SOLUTION = '233168'

MAX_NUM = 1000


def solve():
    num_3s = range(0, MAX_NUM, 3)
    num_5s = range(0, MAX_NUM, 5)
    num_15s = range(0, MAX_NUM, 15)

    total = sum(num_3s) + sum(num_5s) - sum(num_15s)

    return str(total)