from functools import reduce
import operator

MAX_NUM = 100

def solution_01():
    product = reduce(operator.mul, range(1, MAX_NUM + 1))
    product_str = str(product)
    product_digits = list(map(int, product_str))
    return sum(product_digits)