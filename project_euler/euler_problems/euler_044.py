from project_euler.integer import pentagonal, is_pentagonal

SOLUTION = '5482660'


def pentagonal_seq(under=None):
    n = 1
    while True:
        yield pentagonal(n)
        n += 1
        if under is not None and n >= under:
            break


def solve():
    max_num = 10000
    for i in range(1, max_num):
        for j in range(i, max_num):
            pi = pentagonal(i)
            pj = pentagonal(j)
            
            p_sum = pi + pj
            p_diff = pj - pi

            if is_pentagonal(p_sum) and is_pentagonal(p_diff):
                return str(p_diff)

    