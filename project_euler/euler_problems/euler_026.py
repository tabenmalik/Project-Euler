from decimal import Decimal

LARGEST_DENOM = 10

def solution_01():
    for i in range(2, LARGEST_DENOM + 1):
        d = Decimal(1) / Decimal(i)
        print(d)