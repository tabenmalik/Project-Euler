from project_euler.integer import split

SOLUTION = '972'


def solve():
    nums = [x**y for x in range(0, 100) for y in range(0, 100)]

    nums = map(split, nums)
    digit_sums = map(sum, nums)

    return str(max(digit_sums))
