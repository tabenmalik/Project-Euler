from pe.misc import prime_factors

SOLUTION = "134043"


def solve():
    distinct_prime_factors = 4

    consecutive_nums = []
    i = 4
    while True:
        factors = set(prime_factors(i))
        if len(factors) == distinct_prime_factors:
            consecutive_nums.append(i)
            if len(consecutive_nums) == distinct_prime_factors:
                return str(consecutive_nums[0])
        else:
            consecutive_nums = []
        i += 1
