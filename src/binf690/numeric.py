"""Utilities for Numeric Methods.

"""


def machine_epsilon():
    """Return the relative round-off error of floating point arithmetic."""
    x = 1.0
    while 1 < 1.0 + x / 2:
        x /= 2
    return x


eps = machine_epsilon()


def relative_true_error(true_x, x):
    """Return the relative true error"""
    return (true_x - x) / true_x


def is_int(x):
    """Return true if x is an integer"""
    return abs(x - int(x)) < eps
