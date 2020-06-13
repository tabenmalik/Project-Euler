MAX_NUM = 100

def solution_01():
    nums = range(1, MAX_NUM+1)

    sum_of_sqrs = sum(map(lambda x: x ** 2, nums))
    sqr_of_sum = sum(nums) ** 2

    return sqr_of_sum - sum_of_sqrs