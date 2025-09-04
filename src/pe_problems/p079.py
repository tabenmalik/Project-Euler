import os
from collections import defaultdict
from graphlib import TopologicalSorter

from pe.integer import split, concat

SOLUTION = "73162890"


def solve() -> str:
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, "p079.txt")) as fobj:
        attempts = list(map(int, fobj))

    graph: defaultdict[int, set[int]] = defaultdict(set)
    for attempt in attempts:
        digits = split(attempt)
        graph[digits[2]].update(digits[:2])
        graph[digits[1]].update(digits[:1])

    return str(concat(TopologicalSorter(graph).static_order()))
