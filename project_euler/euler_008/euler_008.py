import os
from functools import reduce
import operator

DIGIT_FILE = '1000_digit_num.txt'
ADJ_DIGITS = 13

ANSWER = 23514624000

def read_digit_file():
    this_dir, this_filename = os.path.split(__file__)
    
    digits = []
    with open(os.path.join(this_dir, DIGIT_FILE)) as fhdl:
        for line in fhdl:
            line = line.rstrip()
            line_digits = list(map(int, line))           
            digits.extend(line_digits)

    return digits


def solution_01():
    digits = read_digit_file()
    num_digits = len(digits)
    
    largest_product = 0
    for i in range(num_digits-ADJ_DIGITS):
        adj_digits = digits[i:i+ADJ_DIGITS]
        product = reduce(operator.mul, adj_digits)
        largest_product = max(product, largest_product)

    return largest_product