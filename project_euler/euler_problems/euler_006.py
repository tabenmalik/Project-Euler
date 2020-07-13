from project_euler import misc

SOLUTION = '25164150'

MAX_NUM = 100


def solve():
    """
    Solution provided by Project Euler
    """

    return str(misc.sum_of_n(MAX_NUM) ** 2 - misc.sum_of_sqrs(MAX_NUM))
