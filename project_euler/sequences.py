from collections import abc
import math

from project_euler.misc import divisors


class Triangulars(abc.Iterable, abc.Container):
    """
    Computes the nth trigonal number.
    A trigonal number is number of objects that can be arranged into an
    equilateral triangle.

    Examples:
        0, 1, 3, 6, 10, 15, ...
    """

    def __iter__(self):
        i = 0
        while True:
            yield self[i]
            i += 1

    def __contains__(self, value):
        try:
            self.index(value)
            return True
        except ValueError:
            return False

    def __getitem__(self, n):
        if isinstance(n, slice):
            if n.stop is None:
                raise ValueError("")
            return tuple(self[i] for i in range(n.start or 0, n.stop, n.step or 1))
        
        if n < 0:
            raise IndexError

        return math.comb(n + 1, 2)

    def index(self, value):
        if value < 0:
            raise ValueError

        n_1 = -0.5 + math.sqrt(0.25 + (2 * value))
        n_2 = -0.5 - math.sqrt(0.25 + (2 * value))

        if n_1 >= 0 and self[int(n_1)] == value:
            return int(n_1)
        elif  n_2 >= 0 and self[int(n_2)] == value:
            return int(n_2)
        
        raise ValueError


class Pentagonals:
    """
    Computes the nth pentagonal number.
    Similar to a trigonal number, but instead is about the number for the outline
    of a pentagon, not the area.

    Examples:
        1, 5, 12, 22, 35, 51, ...
    """
    
    def __iter__(self):
        i = 0
        while True:
            yield self[i]
            i += 1

    def __contains__(self, value):
        try:
            self.index(value)
            return True
        except ValueError:
            return False

    def __getitem__(self, n):
        if isinstance(n, slice):
            if n.stop is None:
                raise ValueError("")
            return tuple(self[i] for i in range(n.start or 0, n.stop, n.step or 1))

        if n < 0:
            raise IndexError

        return (n * ((3 * n) - 1)) // 2

    def index(self, value):
        if value < 0:
            raise ValueError

        n_1 = (0.5 + math.sqrt(0.25 + (6 * value))) / 3
        n_2 = (0.5 - math.sqrt(0.25 + (6 * value))) / 3

        if n_1 >= 0 and self[int(n_1)] == value:
            return int(n_1)
        elif n_2 > 0 and self[int(n_2)] == value:
            return int(n_2)

        raise ValueError


class Hexagonals:
    """
    Computes the n_th hexagonal number.
    Similar to a pentagonal number but for the shape of a hexagon.

    Examples:
        1, 6, 15, 28, 45, 66, ...
    """

    def __iter__(self):
        i = 0
        while True:
            yield self[i]
            i += 1

    def __contains__(self, value):
        try:
           self.index(value)
           return True
        except ValueError:
            return False

    def __getitem__(self, n):
        if isinstance(n, slice):
            if n.stop is None:
                raise ValueError("")
            return tuple(self[i] for i in range(n.start or 0, n.stop, n.step or 1))
        return n * ((2 * n) - 1)

    def index(self, value):
        if value <= 0:
            raise ValueError()

        n_1 = 0.25 * (1 + math.sqrt(1 + (8 * value)))
        n_2 = 0.25 * (1 - math.sqrt(1 + (8 * value)))

        if n_1 > 0 and self[int(n_1)] == value:
            return int(n_1)
        elif n_2 > 0 and self[int(n_2)] == value:
            return int(n_2)

        raise ValueError()


def permutations_seq(digits):
    yield digits.copy()

    largest_index_k = 0
    while largest_index_k != -1:
        largest_index_k = -1
        for i in range(len(digits) - 1):
            if digits[i] < digits[i+1]:
                largest_index_k = i

        if largest_index_k != -1:
            largest_index_l = 0
            for l in range(largest_index_k+1, len(digits)):
                if digits[largest_index_k] < digits[l]:
                    largest_index_l = l

            digits[largest_index_k], digits[largest_index_l] = digits[largest_index_l], digits[largest_index_k]
            digits[largest_index_k+1:] = reversed(digits[largest_index_k+1:])
            yield digits.copy()


def prime_seq():
    """
    Prime numbers sequence.
    OEIS A000040
    """
    yield 2

    i = 3
    while True:
        if len(divisors(i)) == 2:
            yield i
        i += 2


def fibonacci_seq(under=None):
    """
    A generator of fibonacci numbers
    """
    fib_1 = 1
    fib_2 = 1

    if under is None or fib_1 < under:
        yield fib_1

    if under is None or fib_2 < under:
        yield fib_2

    fib_new = fib_2 + fib_1
    while under is None or fib_new < under:
        yield fib_new

        fib_1 = fib_2
        fib_2 = fib_new

        fib_new = fib_2 + fib_1


def even_fibonacci_seq():
    """
    Even fibonacci number sequence.
    OEIS A022342
    """
    fib_1 = 2
    fib_2 = 8

    yield fib_1
    yield fib_2

    fib_new = (4 * fib_2) + fib_1
    while True:
        yield fib_new

        fib_1 = fib_2
        fib_2 = fib_new

        fib_new = (4 * fib_2) + fib_1
