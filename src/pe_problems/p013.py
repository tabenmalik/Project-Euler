from __future__ import annotations

from importlib.resources import files

import pe_problems

SOLUTION: str = "5537376230"

NUM_DIGITS: int = 10


def read_number_file() -> tuple[int, ...]:
    lines = files(pe_problems).joinpath("p013.txt").read_text().splitlines()
    return tuple(int(line) for line in lines)


def solve() -> str:
    nums = read_number_file()
    total = sum(nums)
    return str(str(total)[:10])
