from pe.integer import concat, split, ireversed, palindromic

SOLUTION = "249"


def is_lychrel(n: int, iterations: int = 50) -> bool:
    num = n
    for _ in range(0, iterations):
        num += ireversed(num)
        if palindromic(num):
            return False

    return True


def solve() -> str:
    lychrel_nums = list(filter(is_lychrel, range(1, 10_000)))
    return str(len(lychrel_nums))
