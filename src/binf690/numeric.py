"""Utilities for Numeric Methods.

"""


def machine_epsilon():
    """Return the relative round-off error of floating point arithmetic."""
    x = 1.0
    while 1 < 1.0 + x / 2:
        x /= 2
    return x


eps = machine_epsilon()


def is_int(x):
    return abs(x - int(x)) < eps
