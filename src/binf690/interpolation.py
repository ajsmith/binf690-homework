"""Interpolation implementation.

Alexander Smith
BINF690
George Mason University
Fall 2020

"""

from functools import reduce

import numpy as np


def product(xs):
    return reduce(lambda x1, x2: x1 * x2, xs, 1)


class FDD:
    """Finite Divided Difference

    """

    def __init__(self, p0, p1):
        self.x0, self.y0 = p0
        self.x1, self.y1 = p1

    def __call__(self, x):
        return self.y0 + self.slope() * (x - self.x0)

    def slope(self):
        return (self.y1 - self.y0) / (self.x1 - self.x0)


class RecursiveFDD:
    """Recursive Finite Divided Difference and Newton Polynomial"""

    def __init__(self, points, error_point=None):
        if len(points) < 2:
            raise ValueError('At least 2 points needed!')

        if len(points) == 2:
            self.fdd0 = FDD(*points)
            self.fdd1 = None
        else:
            self.fdd0 = RecursiveFDD(points[:-1])
            self.fdd1 = RecursiveFDD(points[1:])

        self.x0, _ = points[0]
        self.xn, _ = points[-1]
        self.xs = [x for (x, _) in points]

        if error_point:
            self.error_fdd = RecursiveFDD(list(points) + [error_point])
        else:
            self.error_fdd = None

        self.order = len(points) - 1

    def __call__(self, x):
        if self.fdd1 is None:
            result = self.fdd0(x)
        else:
            result = self.fdd0(x) + self.polynomial_term(x)
        return result

    def polynomial_term(self, x):
        return self.slope() * product(x - xn for xn in self.xs[:-1])

    def slope(self):
        if self.fdd1 is None:
            return self.fdd0.slope()
        else:
            x0 = self.fdd0.x0
            xn = self.fdd1.xn
            return (self.fdd1.slope() - self.fdd0.slope()) / (xn - x0)

    def error(self, x):
        assert self.error_fdd is not None, 'No error point provided!'
        return self.error_fdd.polynomial_term(x)
