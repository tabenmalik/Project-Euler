from itertools import starmap
from functools import partial
from collections.abc import Iterable
import os
from math import log

import pe_problems
from importlib.resources import files

SOLUTION: str = "709"


def argmax(iterable: Iterable[int]) -> int:
    it = iter(iterable)

    maxi = 0
    maxn = next(it)

    for i, n in enumerate(it, 1):
        if n > maxn:
            maxn = n
            maxi = i

    return maxi


def solve() -> str:
    this_dir, _ = os.path.split(__file__)

    exps = files(pe_problems).joinpath("p099.txt").read_text().splitlines()

    exps = map(partial(str.split, sep=","), exps)
    exps = map(tuple, map(partial(map, int), exps))
    log_exps = starmap(lambda x, e: e * log(x), exps)
    return str(argmax(log_exps) + 1)


if __name__ == "__main__":
    print(solve())
