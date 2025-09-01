from pe.integer import split

SOLUTION = "142857"


def solve() -> str:
    n = 2
    while True:
        n_digits = sorted(split(n))
        for mult in range(2, 7):
            n_mult_digits = sorted(split(n * mult))
            if n_mult_digits != n_digits:
                break
        else:
            return str(n)
        n += 1
