from itertools import count
from math import isqrt



def is_sqr(x):
    return isqrt(x)**2 == x

# def solve():
#     for total in count(int(10**12)):
#         print(total)
#         discr = 4 + 8 * total**2 - 8 * total

#         if not is_sqr(discr):
#             continue

#         root1 = int((2 + isqrt(discr)) / 4)
#     return root1

def quadratic_roots(a, b, c):
    disc = sqrt(b**2 - 4 * a * c)


def solve():
    for square in (i**2 for i in count(isqrt(1 + 2*10**12**2-2*10**12))):
        print(square)
        a = 2
        b = -2
        c = 1 - square

        disc = b**2 - 4 * a * c

        if not is_sqr(disc):
            continue

        y = int((-b + 2*isqrt(disc)) / (2*a))

        x = int(2 + isqrt(4 + 8*y**2 - 8*y) / 4)
        print(x, y)


