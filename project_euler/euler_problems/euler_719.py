import math
import itertools
import operator
from project_euler.integer import digits_of_n
from project_euler.misc import digits_to_num
from functools import partial
import collections


def dotproduct(vec1, vec2):
    return sum(map(operator.mul, vec1, vec2))


# @profile
def convolve(signal, kernel):
    kernel = tuple(kernel)[::-1]
    n = len(kernel)
    window = collections.deque([0], maxlen=n) * n
    for x in signal: #itertools.chain(signal, itertools.repeat(0, n - 1)):
        window.append(x)
        yield dotproduct(kernel, window)

# @profile
def itersplit(iterable, indices):
    iterable = iter(iterable)
    # indices = convolve(indices, (1, -1))
    indices = map(dotproduct, itertools.pairwise(itertools.chain((0,), indices)), itertools.repeat((-1, 1)))
    for stop in itertools.chain(indices, [None]):
        yield tuple(itertools.islice(iterable, stop))


def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))


# @profile
def splits(iterable):
    """
    """
    items = tuple(iterable)
    for indices in powerset(range(1, len(items))):
        yield tuple(itersplit(items, indices))


def square(n):
    """
    A squaring operator. Returns n^2.
    """
    return n*n


def squares(stop=None):
    """
    A generator of squares.
    """
    return map(square, itertools.count())


# @profile
def is_s_number(n):
    """
    """
    sqrt = math.sqrt(n)
    digits = digits_of_n(n)

    for split in splits(digits):
        if sqrt == sum(map(digits_to_num, split)):
            print(n)
            return True
    
    return False
    
def s_numbers():
    return filter(is_s_number, squares())

# @profile
def solve():
    solution = sum(filter(is_s_number, itertools.takewhile(lambda x: x <= 10**12, squares())))
    return solution

if __name__ == "__main__":
    solve()