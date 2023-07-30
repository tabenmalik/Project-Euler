SOLUTION = '73162890'
import os
from collections import defaultdict
from graphlib import TopologicalSorter

from project_euler.integer import split, concat
def solve():
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, "euler_079.txt")) as fobj:
        attempts = list(map(int, fobj))

    graph = defaultdict(set)
    for attempt in attempts:
        digits = split(attempt)
        graph[digits[2]].update(digits[:2])
        graph[digits[1]].update(digits[:1])

    return str(concat(TopologicalSorter(graph).static_order()))
