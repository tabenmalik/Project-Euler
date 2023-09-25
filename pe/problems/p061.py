"""
Cyclical Figurate Numbers
"""

from pe.integer import split
from itertools import takewhile, product


def triangonal(n):
    return (n * (n + 1)) // 2


def square(n):
    return n**2


def pentagonal(n):
    return (n * ((3 * n) - 1)) // 2


def hexagonal(n):
    return n * ((2 * n) - 1)


def heptagonal(n):
    return (n * ((5 * n) - 3)) // 2


def octogonal(n):
    return n * ((3 * n) - 2)


def infrange(start=0, step=1):
    n = start

    while True:
        yield n
        n += step


def get_4_digit_ns_from_seq(func):
    def _under_5_digits(n):
        return len(split(n)) < 5

    def _only_4_digits(n):
        return len(split(n)) == 4

    fns = map(func, infrange(1))
    fns = takewhile(_under_5_digits, fns)
    fns = filter(_only_4_digits, fns)
    fns = list(fns)

    return fns


def is_cycle(nums, full):
    sorted_cycle = [nums[0]]
    nums = list(nums)
    nums.remove(nums[0])

    while len(nums) != 0:
        last_digits = split(sorted_cycle[-1])[-2:]
        for num in nums:
            beginning_digits = split(num)[:2]
            if last_digits == beginning_digits:
                sorted_cycle.append(num)
                nums.remove(num)
                break
        else:
            return False

    if full:
        beginning_digits = split(sorted_cycle[0])[:2]
        last_digits = split(sorted_cycle[-1])[-2:]
        return beginning_digits == last_digits
    else:
        return True


def solve():
    tris = get_4_digit_ns_from_seq(triangonal)
    sqrs = get_4_digit_ns_from_seq(square)
    pens = get_4_digit_ns_from_seq(pentagonal)
    hexs = get_4_digit_ns_from_seq(hexagonal)
    heps = get_4_digit_ns_from_seq(heptagonal)
    octs = get_4_digit_ns_from_seq(octogonal)

    seqs = {
        "tris": list(tris),
        "sqrs": list(sqrs),
        "pens": list(pens),
        "hexs": list(hexs),
        "heps": list(heps),
        "octs": list(octs),
    }

    cycles = [(set(["octs"]), [o]) for o in octs]
    new_cycles = []

    while True:
        for cycle_seqs, cycle in cycles:
            for seq_name, seq in seqs.items():
                if seq_name not in cycle_seqs:
                    for num in seq:
                        if is_cycle(cycle + [num], False):
                            new_cycles.append(
                                (cycle_seqs | set([seq_name]), cycle + [num])
                            )
        cycles = new_cycles
        new_cycles = []

        if len(cycles[0][1]) == 6:
            break

    for _, cycle in cycles:
        if is_cycle(cycle, True):
            print(cycle)
            return str(sum(cycle))
