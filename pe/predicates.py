"""A module of functions to create predicates."""
import operator

def le(n):
    def _unary_le(x):
        return operator.le(x, n)
    return _unary_le

# this can be replace with a "partial"
def lt(n):
    """Creates a less than unary predicate"""
    def _unary_lt(x):
        return operator.lt(x, n)
    return _unary_lt
