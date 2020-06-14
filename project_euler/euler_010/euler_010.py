from project_euler import primes

MAX_NUM = 2_000_000


def solution_01():
    ps = primes.prime_seq(under=MAX_NUM)

    return sum(ps)