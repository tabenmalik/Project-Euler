from __future__ import annotations

import sys
from collections.abc import Iterable
from collections.abc import Iterator
from collections.abc import Sequence
from contextlib import suppress
from itertools import islice
from typing import Any
from typing import cast
from typing import TypeVar

if sys.version_info >= (3, 15):  # pragma: >= 3.15 cover
    from math.integer import isqrt
else:  # pragma: < 3.15 cover
    from math import isqrt

T = TypeVar("T")


def iter_index(
    iterable: Iterable[T],
    value: Any,
    start: int = 0,
    stop: int | None = None,
):
    "Return indices where a value occurs in a sequence or iterable."
    # iter_index('AABCADEAF', 'A') → 0 1 4 7
    seq_index = getattr(iterable, 'index', None)
    if seq_index is None:
        iterator = islice(iterable, start, stop)
        for i, element in enumerate(iterator, start):
            if element is value or element == value:
                yield i
    else:
        iterable = cast(Sequence[T], iterable)
        stop = len(iterable) if stop is None else stop
        i = start
        with suppress(ValueError):
            while True:
                yield (i := seq_index(value, i, stop))
                i += 1


def sieve(n: int) -> Iterator[int]:
    "Primes less than n."
    # sieve(30) → 2 3 5 7 11 13 17 19 23 29
    if n > 2:
        yield 2
    data = bytearray((0, 1)) * (n // 2)
    for p in iter_index(data, 1, start=3, stop=isqrt(n) + 1):
        data[p*p: n: p+p] = bytes(len(range(p*p, n, p+p)))
    yield from iter_index(data, 1, start=3)
