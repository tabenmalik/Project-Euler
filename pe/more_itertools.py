"""
Convienent itertools functions provided by Python docs:
    https://docs.python.org/3/library/itertools.html
"""

from itertools import islice, chain, count, groupby, repeat
from itertools import tee, cycle, zip_longest, filterfalse, combinations
import collections
import operator
import random


def take(n, iterable):
    """
    Return first n items of the iterable as a list.

    Example:
        take(3, [4, 6, 2, 7, 8]) -> 4, 6, 2
    """
    return list(islice(iterable, n))


def prepend(value, iterator):
    """
    Prepend a single value in front of an iterator.

    Example:
        prepend(1, [2, 3, 4]) -> 1 2 3 4
    """
    return chain([value], iterator)


def tabulate(function, start=0):
    """Return function(0), function(1), ..."""
    return map(function, count(start))


def tail(n, iterable):
    """
    Return an iterator over the last n items

    Example:
        tail(3, 'ABCDEFG') -> E F G
    """
    return iter(collections.deque(iterable, maxlen=n))


def consume(iterator, n=None):
    """Advance the iterator n-steps ahead. If n is None, consume entirely."""
    # Use functions that consume iterators at the speed of C.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)


def nth(iterable, n, default=None):
    """Returns the nth item or a default value"""
    return next(islice(iterable, n, None), default)


def all_equal(iterable):
    """Returns True if all the elements are equal to each other"""
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def quantify(iterable, pred=bool):
    """Count how many times the predicate is true"""
    return sum(map(pred, iterable))


def pad_none(iterable):
    """
    Returns the sequence elements and then returns None indefinitely.
    Useful for emulating the behavior of the built-in map() function.
    """
    return chain(iterable, repeat(None))


def ncycles(iterable, n):
    """Returns the sequence elements n times"""
    return chain.from_iterable(repeat(tuple(iterable), n))


def dotproduct(vec1, vec2):
    """
    Computes the dot product of two iterables.
    Dot proudct is defined as:
        vec1 . vec2 = vec1[0]*vec2[0] + vec1[1]*vec2[1] + ...
    """
    return sum(map(operator.mul, vec1, vec2))


def convolve(signal, kernel):
    """
    Convolves the signal iterable using the provided kernel
    See:  https://betterexplained.com/articles/intuitive-convolution/

    Examples:
        convolve(data, [0.25, 0.25, 0.25, 0.25]) --> Moving average (blur)
        convolve(data, [1, -1]) --> 1st finite difference (1st derivative)
        convolve(data, [1, -2, 1]) --> 2nd finite difference (2nd derivative)
    """
    kernel = tuple(kernel)[::-1]
    n = len(kernel)
    window = collections.deque([0], maxlen=n) * n
    for x in chain(signal, repeat(0, n - 1)):
        window.append(x)
        yield sum(map(operator.mul, kernel, window))


def flatten(list_of_lists):
    """Flatten one level of nesting"""
    return chain.from_iterable(list_of_lists)


# def repeatfunc(func, times=None, *args):
#     """
#     Repeat calls to func with specified arguments.

#     Example:
#         repeatfunc(random.random)
#     """
#     if times is None:
#         return starmap(func, repeat(args))
#     return starmap(func, repeat(args, times))


def pairwise(iterable):
    """
    Create pairs of two consecutive elements from the iterable.

    Example:
        s -> (s0,s1), (s1,s2), (s2, s3), ...
    """
    a, b = tee(iterable)
    next(b, default=None)
    return zip(a, b)


def grouper(iterable, n, fillvalue=None):
    """
    Collect data into fixed-length chunks or blocks

    Examples:
        grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    """
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def roundrobin(*iterables):
    """
    Consume all iterables in round robin fashion.

    Example:
        roundrobin('ABC', 'D', 'EF') --> A D E B F C
    """
    # Recipe credited to George Sakkis
    num_active = len(iterables)
    nexts = cycle(iter(it).__next__ for it in iterables)
    while num_active:
        try:
            for nxt in nexts:
                yield nxt()
        except StopIteration:
            # Remove the iterator we just exhausted from the cycle.
            num_active -= 1
            nexts = cycle(islice(nexts, num_active))


def partition(pred, iterable):
    """
    Use a predicate to partition entries into false entries and true entries

    Examples:
        partition(is_odd, range(10)) --> 0 2 4 6 8   and  1 3 5 7 9
    """
    t_1, t_2 = tee(iterable)
    return filterfalse(pred, t_1), filter(pred, t_2)


def powerset(iterable):
    """
    Return all possible sets created from the iterable elements

    Examples:
        powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def unique_everseen(iterable, key=None):
    """
    List unique elements, preserving order. Remember all elements ever seen.

    Examples:
        unique_everseen('AAAABBBCCDAABBB') --> A B C D
        unique_everseen('ABBCcAD', str.lower) --> A B C D
    """
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element


def unique_justseen(iterable, key=None):
    """
    List unique elements, preserving order. Remember only the element just seen.

    Examples:
        unique_justseen('AAAABBBCCDAABBB') --> A B C D A B
        unique_justseen('ABBCcAD', str.lower) --> A B C A D
    """
    return map(next, map(operator.itemgetter(1), groupby(iterable, key)))


def iter_except(func, exception, first=None):
    """
    Call a function repeatedly until an exception is raised.

    Converts a call-until-exception interface to an iterator interface.
    Like builtins.iter(func, sentinel) but uses an exception instead
    of a sentinel to end the loop.

    Examples:
        iter_except(functools.partial(heappop, h), IndexError)   # priority queue iterator
        iter_except(d.popitem, KeyError)                         # non-blocking dict iterator
        iter_except(d.popleft, IndexError)                       # non-blocking deque iterator
        iter_except(q.get_nowait, Queue.Empty)                   # loop over a producer Queue
        iter_except(s.pop, KeyError)                             # non-blocking set iterator

    """
    try:
        if first is not None:
            yield first()  # For database APIs needing an initial cast to db.first()
        while True:
            yield func()
    except exception:
        pass


def first_true(iterable, default=False, pred=None):
    """
    Returns the first true value in the iterable.

    If no true value is found, returns *default*

    If *pred* is not None, returns the first item
    for which pred(item) is true.

    Examples:
        first_true([a,b,c], x) --> a or b or c or x
        first_true([a,b], x, f) --> a if f(a) else b if f(b) else x
    """
    return next(filter(pred, iterable), default)


# def random_product(*args, repeat=1):
#     """Random selection from itertools.product(*args, **kwds)"""
#     pools = [tuple(pool) for pool in args] * repeat
#     return tuple(map(random.choice, pools))


def random_permutation(iterable, r=None):
    """Random selection from itertools.permutations(iterable, r)"""
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(random.sample(pool, r))


def random_combination(iterable, r):
    """Random selection from itertools.combinations(iterable, r)"""
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.sample(range(n), r))
    return tuple(pool[i] for i in indices)


def random_combination_with_replacement(iterable, r):
    """Random selection from itertools.combinations_with_replacement(iterable, r)"""
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.choices(range(n), k=r))
    return tuple(pool[i] for i in indices)


def nth_combination(iterable, r, index):
    """Equivalent to list(combinations(iterable, r))[index]"""
    pool = tuple(iterable)
    n = len(pool)
    if r < 0 or r > n:
        raise ValueError
    c = 1
    k = min(r, n - r)
    for i in range(1, k + 1):
        c = c * (n - k + i) // i
    if index < 0:
        index += c
    if index < 0 or index >= c:
        raise IndexError
    result = []
    while r:
        c, n, r = c * r // n, n - 1, r - 1
        while index >= c:
            index -= c
            c, n = c * (n - r) // n, n - 1
        result.append(pool[-1 - n])
    return tuple(result)


def rolling(iterable, func, window_size=1):
    """Applies a function over a rolling window of the iterable elements"""
    window = collections.deque(take(window_size - 1, iterable), maxlen=window_size)

    for x in iterable:
        window.append(x)
        yield func(*window)


def arg_expander(func):
    def _funkier(iterable):
        return func(*iterable)

    return _funkier
