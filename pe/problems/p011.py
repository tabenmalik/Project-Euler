import os
from functools import reduce
import operator



NUM_GRID_FILE = 'p011.txt'
ADJ_NUMS = 4


def read_grid_file():
    this_dir, _ = os.path.split(__file__)
    
    num_matrix = []
    with open(os.path.join(this_dir, NUM_GRID_FILE)) as fhdl:
        for line in fhdl:
            line = line.rstrip()
            nums = line.split(' ')
            line_nums = list(map(int, nums))           
            num_matrix.append(line_nums)

    return num_matrix


def solve():
    num_matrix = read_grid_file()
    nrows = len(num_matrix)
    ncols = len(num_matrix[0])

    greatest_product = 0

    for row in range(0, nrows):
        for col in range(0, ncols-ADJ_NUMS):
            adj_nums = num_matrix[row][col:col+ADJ_NUMS]
            product = reduce(operator.mul, adj_nums)
            greatest_product = max(greatest_product, product)

    for row in range(0, nrows-ADJ_NUMS):
        for col in range(0, ncols):
            adj_nums = [num_matrix[row+i][col] for i in range(ADJ_NUMS)]
            product = reduce(operator.mul, adj_nums)
            greatest_product = max(greatest_product, product)

    for row in range(0, nrows-ADJ_NUMS):
        for col in range(0, ncols-ADJ_NUMS):
            adj_nums = [num_matrix[row+i][col+i] for i in range(ADJ_NUMS)]
            product = reduce(operator.mul, adj_nums)
            greatest_product = max(greatest_product, product)

    for row in range(0, nrows-ADJ_NUMS):
        for col in range(ADJ_NUMS-1, ncols):
            adj_nums = [num_matrix[row+i][col-i] for i in range(ADJ_NUMS)]
            product = reduce(operator.mul, adj_nums)
            greatest_product = max(greatest_product, product)

    
    return str(greatest_product)
