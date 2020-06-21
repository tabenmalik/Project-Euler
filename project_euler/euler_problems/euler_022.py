import os
import operator

SOLUTION = 871198282
NUM_FILE = 'euler_022.txt'

def read_name_file():
    this_dir, _ = os.path.split(__file__)
    
    names = ''
    with open(os.path.join(this_dir, NUM_FILE)) as fhdl:
        line = fhdl.read()
        line = line.rstrip()
        line = line.replace('"', '')
        names = line.split(',')

    return names


def alphabetical_value(string):
    return sum(map(lambda x: x - ord('a') + 1, map(ord, string.lower())))

def solution_01():
    names = read_name_file()
    names = sorted(names)
    name_values = map(alphabetical_value, names)
    name_values = map(lambda x: x[0]*x[1], enumerate(name_values, start=1))
    return sum(name_values)

