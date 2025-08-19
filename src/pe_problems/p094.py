from itertools import takewhile
from math import sqrt
from math import isqrt
from itertools import count

SOLUTION = "518408346"

def is_square(n):
    return isqrt(n) * isqrt(n) == n


def perimeter(triangle):
    return triangle[0] + triangle[1] + triangle[2]

def area(triangle):
    return 0.5 * triangle[2] * sqrt(triangle[0] ** 2 - (triangle[2] / 2) ** 2)

def solve() -> str:
    total = 0
    for p in count(2):
        d = 1 + 3 * (p**2)
        if not is_square(d):
            continue
        root_d = isqrt(d)
        for offset in {-1, 1}:
            for sign in {1, -1}:
                f = (-4 * offset) + (sign * 2 * root_d)
                if f < 1 or f % 3 != 0:
                    continue
                c = f // 3
                a = offset + c
                perim = 2 * a + c
                if perim > 1_000_000_000:
                    return str(total)
                print((a, a, c), perim, area((a, a, c)))
                total += perim
    return str(total)


if __name__ == "__main__":
    solution = solve()
    print(solution)
    raise SystemExit(solution == SOLUTION)
