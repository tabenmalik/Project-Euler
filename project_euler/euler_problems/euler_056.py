from project_euler.misc import num_to_digits

SOLUTION = '972'


def solve():
    nums = [x**y for x in range(0, 100) for y in range(0, 100)]

    nums = map(num_to_digits, nums)
    digit_sums = map(sum, nums)

    return str(max(digit_sums))
