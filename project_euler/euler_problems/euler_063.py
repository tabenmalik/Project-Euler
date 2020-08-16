from itertools import count, takewhile

from project_euler.misc import num_to_digits

SOLUTION = '49'

def positive_integers_seq(start=1, step=1):
    return count(start, step)

def solve():
    n = 1
    total = 0
    while True:
        nums = map(lambda i: i**n, positive_integers_seq())
        nums = takewhile(lambda num: len(num_to_digits(num)) <= n, nums)
        nums = filter(lambda num: len(num_to_digits(num)) == n, nums)

        subtotal = len(list(nums))
        if subtotal == 0:
            break
        total += subtotal
        n += 1

    return str(total)
