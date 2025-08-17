import os
import operator
import pe_problems
from importlib.resources import files

SOLUTION: str = "871198282"


def read_name_file() -> list[str]:
    this_dir, _ = os.path.split(__file__)
    line = files(pe_problems).joinpath("p022.txt").read_text()
    line = line.rstrip()
    line = line.replace('"', "")
    names = line.split(",")
    return names


def alphabetical_value(string: str) -> int:
    return sum(map(lambda x: x - ord("a") + 1, map(ord, string.lower())))


def solve() -> str:
    names = read_name_file()
    names = sorted(names)
    name_values = map(alphabetical_value, names)
    name_values = map(lambda x: x[0] * x[1], enumerate(name_values, start=1))
    return str(sum(name_values))
