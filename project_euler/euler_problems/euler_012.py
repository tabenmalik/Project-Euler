from project_euler.misc import sum_of_n, divisors

SOLUTION = '76576500'

NUM_DIVISORS = 500


def triangle_num_seq():
    n = 1
    while True:
        yield sum_of_n(n)
        n += 1


def solve():
    triangle_nums = triangle_num_seq()

    for triangle_num in triangle_nums:
        num_divisors = len(divisors(triangle_num))
        if num_divisors > NUM_DIVISORS:
            break
    
    return str(triangle_num)
