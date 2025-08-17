"""A module of functions to create predicates."""

import operator
from typing import Callable
from typing import Any


def le(n: Any) -> Callable[[Any], Any]:
    def _unary_le(x: Any) -> Any:
        return operator.le(x, n)

    return _unary_le


# this can be replace with a "partial"
def lt(n: Any) -> Callable[[Any], Any]:
    """Creates a less than unary predicate"""

    def _unary_lt(x: Any) -> Any:
        return operator.lt(x, n)

    return _unary_lt
