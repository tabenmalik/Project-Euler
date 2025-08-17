"""
Convienent itertools functions provided by Python docs:
    https://docs.python.org/3/library/itertools.html
"""

from itertools import islice, chain, count, groupby, repeat
from itertools import tee, cycle, zip_longest, filterfalse, combinations
import collections
import operator
import random
from typing import Iterable
from typing import Iterator
from typing import Any
from typing import Callable
from typing import Optional
from typing import cast
from typing import ParamSpec
from typing import TypeVar


def take(n: int, iterable: Iterable[Any]) -> Any:
    """
    Return first n items of the iterable as a list.

    Example:
        take(3, [4, 6, 2, 7, 8]) -> 4, 6, 2
    """
    return list(islice(iterable, n))


def nth(iterable: Iterable[Any], n: int, default: Any = None) -> Any:
    """Returns the nth item or a default value"""
    return next(islice(iterable, n, None), default)


def first_true(
    iterable: Iterable[Any],
    default: bool = False,
    pred: Optional[Callable[[Any], bool]] = None,
) -> Any:
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


R = TypeVar("R")


def rolling(
    iterable: Iterable[Any], func: Callable[..., R], window_size: int = 1
) -> Iterable[R]:
    """Applies a function over a rolling window of the iterable elements"""
    window = collections.deque(take(window_size - 1, iterable), maxlen=window_size)

    for x in iterable:
        window.append(x)
        yield func(*window)


def arg_expander(func: Callable[..., R]) -> Callable[[Iterable[Any]], R]:
    def _funkier(iterable: Iterable[Any]) -> R:
        return func(*iterable)

    return _funkier
