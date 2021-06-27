from project_euler.integer import sum_of_1_to_n, sum_of_sqrs

SOLUTION = '25164150'

MAX_NUM = 100


def solve():
    """
    Solution provided by Project Euler
    """

    return str(sum_of_1_to_n(MAX_NUM) ** 2 - sum_of_sqrs(MAX_NUM))
