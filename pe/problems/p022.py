"""
Names Scores
"""

import os
import operator
import pe.data
from importlib.resources import files


def read_name_file():
    this_dir, _ = os.path.split(__file__)

    names = ""
    line = files(pe.data).joinpath("p022.txt").read_text()
    line = line.rstrip()
    line = line.replace('"', "")
    names = line.split(",")

    return names


def alphabetical_value(string):
    return sum(map(lambda x: x - ord("a") + 1, map(ord, string.lower())))


def solve():
    names = read_name_file()
    names = sorted(names)
    name_values = map(alphabetical_value, names)
    name_values = map(lambda x: x[0] * x[1], enumerate(name_values, start=1))
    return str(sum(name_values))
