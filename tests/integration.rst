===========
Integration
===========

The `is_odd()` helper function checks whether an integer is odd.

    >>> from binf690.integration import is_odd
    >>> is_odd(0.1)
    Traceback (most recent call last):
    ...
    AssertionError: n must be an integer!
    >>> is_odd(0) or is_odd(2) or is_odd(-2)
    False
    >>> is_odd(1)
    True
    >>> is_odd(-1)
    True

The `pairs()` helper returns the items in a list grouped as pairs.

    >>> from binf690.integration import pairs
    >>> list(pairs(range(10)))
    [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
