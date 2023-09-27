"""
Multiples of 3 or 5

.. raw:: html
   :url: https://projecteuler.net/minimal=001

If we list all the natural numbers below :math:`10` that are multiples of 
:math:`3` or :math:`5`, we get :math:`3, 5, 6` and :math:`9`. 
The sum of these multiples is :math:`23`.

Find the sum of all the multiples of :math:`3` or :math:`5` below math:`1000`.
"""

MAX_NUM = 1000


def solve():
    """Solves Project Euler problem 001"""
    num_3s = range(0, MAX_NUM, 3)
    num_5s = range(0, MAX_NUM, 5)
    num_15s = range(0, MAX_NUM, 15)

    total = sum(num_3s) + sum(num_5s) - sum(num_15s)

    return str(total)
