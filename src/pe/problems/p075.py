from collections import Counter
from pprint import pprint
from itertools import count
from math import gcd

SOLUTION = "161667"

def solve():
    p_counts = Counter()

    limit = 1_500_000
    for m in count(2):
        nope = True
        for n in range(m % 2 + 1, m, 2):
            if gcd(n, m) != 1:
                continue
            m2 = m**2
            n2 = n**2

            a = m2 - n2
            b = 2 * m * n
            c = m2 + n2
            p = a + b + c

            k = 1
            while k * p < limit:
                nope = False
                p_counts[k * p] += 1
                k += 1
        if nope:
            break

    return str(Counter(p_counts.values())[1])
