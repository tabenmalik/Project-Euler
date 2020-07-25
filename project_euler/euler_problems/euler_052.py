from project_euler.misc import num_to_digits

SOLUTION = '142857'


def solve():
    n = 2
    while True:
        n_digits = sorted(num_to_digits(n))
        for mult in range(2, 7):
            n_mult_digits = sorted(num_to_digits(n*mult))
            if n_mult_digits != n_digits:
                break
        else:
            return str(n)
        n += 1