"""filter-obj: filter object (dict) keys and values with a simple predicate."""

from __future__ import annotations

from typing import Callable, Mapping, TypeVar

__all__ = ["filter_obj", "__version__"]
__version__ = "0.1.0"

K = TypeVar("K")
V = TypeVar("V")


def filter_obj(
    obj: Mapping[K, V],
    predicate: Callable[[K, V], bool],
) -> dict[K, V]:
    """Return a new dict containing the (key, value) pairs of ``obj`` for
    which ``predicate(key, value)`` is truthy.

    Example
    -------
    >>> filter_obj({"a": 1, "b": 2, "c": 3}, lambda k, v: v > 1)
    {'b': 2, 'c': 3}
    """
    return {key: value for key, value in obj.items() if predicate(key, value)}
