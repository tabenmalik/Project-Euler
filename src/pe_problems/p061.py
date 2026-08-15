from __future__ import annotations

from collections.abc import Callable
from collections.abc import Generator
from collections.abc import Iterator
from collections.abc import Sequence
from itertools import count

from pe.integer import split

SOLUTION = "28684"


def triangonal(n: int) -> int:
    return (n * (n + 1)) // 2


def square(n: int) -> int:
    return n**2


def pentagonal(n: int) -> int:
    return (n * ((3 * n) - 1)) // 2


def hexagonal(n: int) -> int:
    return n * ((2 * n) - 1)


def heptagonal(n: int) -> int:
    return (n * ((5 * n) - 3)) // 2


def octogonal(n: int) -> int:
    return n * ((3 * n) - 2)


def infrange(start: int = 0, step: int = 1) -> Generator[int]:
    n = start

    while True:
        yield n
        n += step


def get_4_digit_ns_from_seq(func: Callable[[int], int]) -> Iterator[int]:
    for x in count(1):
        num = func(x)
        num_digits = split(num)
        if len(num_digits) == 4:
            yield num
        elif len(num_digits) > 4:
            break


def is_cycle(nums: Sequence[int], full: bool) -> bool:
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


def solve() -> str:
    tris = get_4_digit_ns_from_seq(triangonal)
    sqrs = get_4_digit_ns_from_seq(square)
    pens = get_4_digit_ns_from_seq(pentagonal)
    hexs = get_4_digit_ns_from_seq(hexagonal)
    heps = get_4_digit_ns_from_seq(heptagonal)
    octs = list(get_4_digit_ns_from_seq(octogonal))

    seqs = {
        "tris": list(tris),
        "sqrs": list(sqrs),
        "pens": list(pens),
        "hexs": list(hexs),
        "heps": list(heps),
        "octs": list(octs),
    }

    cycles = [({"octs"}, [o]) for o in octs]
    new_cycles = []

    while True:
        for cycle_seqs, cycle in cycles:
            for seq_name, seq in seqs.items():
                if seq_name not in cycle_seqs:
                    for num in seq:
                        if is_cycle(cycle + [num], False):
                            new_cycles.append(
                                (cycle_seqs | {seq_name}, cycle + [num]),
                            )
        cycles = new_cycles
        new_cycles = []

        if len(cycles[0][1]) == 6:
            break

    for _, cycle in cycles:
        if is_cycle(cycle, True):
            return str(sum(cycle))

    return ""
