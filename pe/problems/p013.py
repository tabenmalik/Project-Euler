"""
Large Sum
"""

import os
import pe.data
from importlib.resources import files

NUM_DIGITS = 10


def read_number_file():
    this_dir, _ = os.path.split(__file__)

    num_matrix = []
    lines = files(pe.data).joinpath("p013.txt").read_text().splitlines()
    for line in lines:
        line = line.rstrip()
        line_digits = list(map(int, line))
        num_matrix.append(line_digits)

    return num_matrix


def solve():
    num_matrix = read_number_file()

    num_strs = map(lambda arr: "".join(str(d) for d in arr), num_matrix)
    num_ints = map(int, num_strs)
    num_ints = list(num_ints)

    num_sum = sum(num_ints)

    return str(str(num_sum)[:10])
