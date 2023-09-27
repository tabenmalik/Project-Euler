"""
Counting Sundays

.. raw:: html
   :url: https://projecteuler.net/minimal=019
"""

import datetime as dt


def solve():
    count = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            date = dt.datetime(year, month, 1)
            if date.weekday() == 6:
                count += 1

    return str(count)
