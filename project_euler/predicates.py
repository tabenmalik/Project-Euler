"""A module of functions to create predicates."""
import operator

# this can be replace with a "partial"
def lt(n):
    """Creates a less than unary predicate"""
    def _unary_lt(x):
        return operator.lt(x, n)
    return _unary_lt
