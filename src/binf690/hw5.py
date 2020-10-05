"""Homework 5

Alexander Smith
BINF690
George Mason University
Fall 2020
"""

from binf690.gradient import gradient_descent
from binf690.numeric import eps


def f(x, y):
    """Original function"""
    return -8 * x + x**2 + 12 * y + 4 * y**2 - 2 * x * y


def dfdx(x, y):
    """First order partial derivative with respect to x"""
    return -8 + 2 * x - 2 * y


def dfdy(x, y):
    """First order partial derivative with respect to y"""
    return 12 + 8 * y - 2 * x


def d2fdx2(x, y):
    """Second order partial derivative with respect to x"""
    return 2


def d2fdy2(x, y):
    """Second order partial derivative with respect to y"""
    return 8


def d2fdxdy(x, y):
    """Second order partial derivative with respect to x then y"""
    return -2


def hw5(init=(0.0, 0.0)):
    """Compute and print the numeric solution"""
    gradient_descent(f, dfdx, dfdy, d2fdx2, d2fdy2, d2fdxdy, init)
