from project_euler import misc

ANSWER = 142913828922

MAX_NUM = 2_000_000


def solution_01():
    ps = misc.prime_seq(under=MAX_NUM)

    return sum(ps)