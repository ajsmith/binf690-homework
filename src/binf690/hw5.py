"""Homework 5

Alexander Smith
BINF690
George Mason University
Fall 2020
"""

from binf690.gradient import gradient_descent
from binf690.numeric import eps


def f(x, y):
    return -8 * x + x**2 + 12 * y + 4 * y**2 - 2 * x * y


def dfdx(x, y):
    return -8 + 2 * x - 2 * y


def dfdy(x, y):
    return 12 + 8 * y - 2 * x


def d2fdx2(x, y):
    """Second order partial derivative with respect to x"""
    return 2


def d2fdy2(x, y):
    """Second order partial derivative with respect to y"""
    return 8


def d2fdxdy(x, y):
    """Second order partial derivative with respect to x and y"""
    return -2


def hw5():
    """Compute and print the numeric solution"""
    x, y = (0.0, 0.0)
    gradient_descent(f, dfdx, dfdy, d2fdx2, d2fdy2, d2fdxdy, (x, y))
