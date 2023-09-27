"""
Number Spiral Diagonals

.. raw:: html
   :url: https://projecteuler.net/minimal=028
"""

GRID_SIZE = 1001

#  *1
#   2,  *3,  4,  *5,  6,  *7,  8,  *9
#  10,  11,  12, *13, 14, 15, 16,  *17, 18, 19, 20, 21, 22, 23, 24, 25
# 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40...


def solve():
    up_right = (i**2 for i in range(1, GRID_SIZE + 1, 2))
    up_left = ((i**2) - (i - 1) for i in range(1, GRID_SIZE + 1, 2))
    down_left = ((i**2) - (2 * i - 2) for i in range(1, GRID_SIZE + 1, 2))
    down_right = ((i**2) - (3 * i - 3) for i in range(1, GRID_SIZE + 1, 2))

    total = sum(map(sum, [up_left, up_right, down_left, down_right]))
    total -= 3  # 1 is counted multiple times
    return str(total)
