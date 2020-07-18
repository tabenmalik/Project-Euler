import math
import itertools

from project_euler.integer import sum_of_n

SOLUTION = '4179871'

MAX_NUM = 28123       

def proper_divisors(n):
    if n == 1:
        return []

    divisors = []
    divisors.append(1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            j = n // i
            if j != i:
                divisors.append(j)
    return sorted(divisors)


def is_abundant(n):
    return sum(proper_divisors(n)) > n

def solve():
    abundant_nums = list(filter(is_abundant, range(2, MAX_NUM+1)))
    abundant_num_pairs = ((num, num2) for i, num in enumerate(abundant_nums) for num2 in abundant_nums[i:])
    
    abundant_sums = set(map(sum, abundant_num_pairs))
    abundant_sums = filter(lambda x: x <= (MAX_NUM), abundant_sums)
    abundant_sums = sorted(list(abundant_sums))
    non_abundant_sum = sum_of_n(MAX_NUM) - sum(abundant_sums)

    return str(non_abundant_sum)
