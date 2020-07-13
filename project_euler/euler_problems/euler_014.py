SOLUTION = '837799'

MAX_NUM = 1_000_000
CACHED_LENGTHS = {}


def collatz_len(n):
    if n == 1:
        return 1

    if n in CACHED_LENGTHS:
        return CACHED_LENGTHS[n]

    new_n = n
    if n % 2 == 0:
        new_n = n / 2
    else:
        new_n = (3 * n) + 1

    len = 1 + collatz_len(int(new_n))
    CACHED_LENGTHS[n] = len

    return len

def solution_01():
    _ = list(collatz_len(i) for i in range(1, MAX_NUM))
    
    longest_chain = 0
    n_of_longest_chain = 0
    for k, v in CACHED_LENGTHS.items():
        if v > longest_chain:
            longest_chain = v
            n_of_longest_chain = k

    return n_of_longest_chain


def solution_02():
    _ = list(collatz_len(i) for i in range(500_000, MAX_NUM))
    
    longest_chain = 0
    n_of_longest_chain = 0
    for k, v in CACHED_LENGTHS.items():
        if v > longest_chain:
            longest_chain = v
            n_of_longest_chain = k

    return n_of_longest_chain


def collatz_len_optimized(n):
    if n == 1:
        return 1

    if n in CACHED_LENGTHS:
        return CACHED_LENGTHS[n]

    len = 0
    if n % 2 == 0:
        len = 1 + collatz_len_optimized(int(n / 2))
    else:
        new_n = ((3 * n) + 1) / 2
        len = 2 + collatz_len_optimized(int(new_n))

    CACHED_LENGTHS[n] = len

    return len


def solution_03():
    _ = list(collatz_len_optimized(i) for i in range(500_000, MAX_NUM))
    
    longest_chain = 0
    n_of_longest_chain = 0
    for k, v in CACHED_LENGTHS.items():
        if v > longest_chain:
            longest_chain = v
            n_of_longest_chain = k

    return n_of_longest_chain


def solve():
    return str(solution_03())