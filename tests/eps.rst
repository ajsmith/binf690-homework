===============
Machine Epsilon
===============

The `eps()` function estimates the machine epsilon, which is an upper
bound of the rounding error which can occur with floating point
arithmetic.

    >>> from binf690.numeric import eps
    >>> eps / 2 > 0
    True
    >>> eps / 2 + 1.0 > 1.0
    False
