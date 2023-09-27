"""
Power Digit Sum

.. raw:: html
   :url: https://projecteuler.net/minimal=016
"""

def solve():
    num = 2**1000
    num_str = str(num)
    digits = list(map(int, num_str))
    return str(sum(digits))
