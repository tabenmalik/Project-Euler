import os

SOLUTION = '5537376230'

NUM_GRID_FILE = 'euler_013.txt'
NUM_DIGITS = 10

def read_number_file():
    this_dir, _ = os.path.split(__file__)
    
    num_matrix = []
    with open(os.path.join(this_dir, NUM_GRID_FILE)) as fhdl:
        for line in fhdl:
            line = line.rstrip()
            line_digits = list(map(int, line))           
            num_matrix.append(line_digits)

    return num_matrix


def solve():
    num_matrix = read_number_file()
    
    num_strs = map(lambda arr: ''.join(str(d) for d in arr), num_matrix)
    num_ints = map(int, num_strs)
    num_ints = list(num_ints)

    num_sum = sum(num_ints)

    return str(str(num_sum)[:10])
