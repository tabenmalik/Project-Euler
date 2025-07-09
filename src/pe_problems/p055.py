from pe.integer import concat, split, ireversed, palindromic

SOLUTION = "249"


def is_lychrel(n, iterations=50):
    num = n
    for _ in range(0, iterations):
        num += ireversed(num)
        if palindromic(num):
            return False

    return True


def solve():
    lychrel_nums = list(filter(is_lychrel, range(1, 10_000)))
    return str(len(lychrel_nums))
