import datetime as dt

SOLUTION = '171'

def solution_01():
    count = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            date = dt.datetime(year, month, 1)
            if date.weekday() == 6:
                count += 1

    return count


def solve():
    return str(solution_01())