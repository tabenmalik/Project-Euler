"""
Integer Right Triangles
"""

import pprint


def solve():
    p_solutions = {}

    limit = 1000

    for n in range(1, limit):
        for m in range(n + 1, limit):
            a = (m**2) - (n**2)
            b = 2 * m * n
            c = (m**2) + (n**2)
            p = a + b + c
            k = 1
            while k * p <= limit:
                if k * p not in p_solutions:
                    p_solutions[k * p] = set()

                sorted_triplet = tuple(sorted((k * a, k * b, k * c)))
                p_solutions[k * p].add(sorted_triplet)

                k += 1

    p_solutions = {k: len(v) for k, v in p_solutions.items()}
    return str(max(p_solutions.keys(), key=lambda x: p_solutions[x]))
