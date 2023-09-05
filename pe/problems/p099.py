from itertools import starmap
from functools import partial
import os
from math import log



def argmax(iterable):
    it = iter(iterable)

    maxi = 0
    maxn = next(it)

    for i, n in enumerate(it, 1):
        if n > maxn:
            maxn = n
            maxi = i

    return maxi

def solve():
    this_dir, _ = os.path.split(__file__)

    with open(os.path.join(this_dir, "p099.txt")) as fobj:
        exps = list(fobj)

    exps = map(partial(str.split, sep=','), exps)
    exps = map(tuple, map(partial(map, int), exps))
    log_exps = starmap(lambda x, e: e*log(x), exps)
    return str(argmax(log_exps) + 1)
