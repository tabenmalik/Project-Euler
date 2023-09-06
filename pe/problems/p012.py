from pe.misc import divisors
from pe.integer import sum_of_1_to_n


NUM_DIVISORS = 500


def triangle_num_seq():
    n = 1
    while True:
        yield sum_of_1_to_n(n)
        n += 1


def solve():
    triangle_nums = triangle_num_seq()

    for triangle_num in triangle_nums:
        num_divisors = len(divisors(triangle_num))
        if num_divisors > NUM_DIVISORS:
            break

    return str(triangle_num)
