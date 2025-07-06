import math

SOLUTION = "872187"


def is_palindrome(string):
    reverse_str = string[::-1]
    return string == reverse_str


def to_bin_str(num):
    return bin(num)[2:]


def solve():
    limit = 1_000_000

    num_to_bin_strs = [(str(i), to_bin_str(i)) for i in range(limit)]
    double_palindromes = filter(
        lambda x: is_palindrome(x[0]) and is_palindrome(x[1]), num_to_bin_strs
    )
    ints = next(iter(zip(*double_palindromes)))
    ints = map(int, ints)

    return str(sum(ints))
