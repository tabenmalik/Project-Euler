from project_euler.misc import num_to_digits, digits_to_num
SOLUTION = None


def solve():
    powers = map(lambda x: x**x, range(1, 1000))
    power_sum = sum(powers)

    return str(digits_to_num(num_to_digits(power_sum)[-10:]))