=============================
Utilities for Numeric Methods
=============================

    >>> from binf690.numeric import is_int, eps
    >>> is_int(-1)
    True
    >>> is_int(0)
    True
    >>> is_int(1)
    True
    >>> is_int(-0.5)
    False
    >>> is_int(0.5)
    False
