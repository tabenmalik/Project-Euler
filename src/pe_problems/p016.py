from __future__ import annotations
SOLUTION: str = "1366"


def solve() -> str:
    num = 2**1000
    num_str = str(num)
    digits = list(map(int, num_str))
    return str(sum(digits))
