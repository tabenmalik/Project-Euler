from functools import reduce
import operator

SOLUTION = "648"


MAX_NUM = 100


def solve():
    product = reduce(operator.mul, range(1, MAX_NUM + 1))
    product_str = str(product)
    product_digits = list(map(int, product_str))
    return str(sum(product_digits))
