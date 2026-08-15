from __future__ import annotations

SOLUTION = "872187"


def is_palindrome(string: str) -> bool:
    reverse_str = string[::-1]
    return string == reverse_str


def to_bin_str(num: int) -> str:
    return bin(num)[2:]


def solve() -> str:
    limit = 1_000_000

    total = 0
    for n in range(limit):
        n_str = str(n)
        n_bin_str = to_bin_str(n)
        if is_palindrome(n_str) and is_palindrome(n_bin_str):
            total += n
    return str(total)
