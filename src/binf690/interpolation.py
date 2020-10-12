"""Interpolation implementation.

Alexander Smith
BINF690
George Mason University
Fall 2020

"""

from functools import reduce

import numpy as np


def product(X):
    return reduce(lambda x1, x2: x1 * x2, X, 1)


class LinearInterpolation:

    order = 1

    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1

    def predict(self, x):
        (_, y0) = self.p0
        return (y0 + self.fdd() * (x - x0), None)

    def newton_term_list(self):
        return [self.newton_term()]

    def newton_term(self):
        (x0, _) = self.p0
        return lambda x: self.fdd() * (x - x0)

    def fdd(self):
        x0, y0 = self.p0
        x1, y1 = self.p1
        return (y1 - y0) / (x1 - x0)


class RecursiveNewtonPolynomial:

    def __init__(self, X, Y, error_point=None):
        assert len(X) > 2, 'Must have more than 2 data points!'
        assert len(X) == len(Y), 'X and Y arrays must map to each other!'

        self.X = X
        self.Y = Y
        self.order = len(X) - 1

        if len(X) == 3:
            p0, p1, p2 = tuple(zip(X, Y))
            self.fdd1 = LinearInterpolation(p0, p1)
            self.fdd2 = LinearInterpolation(p1, p2)
        else:
            self.fdd1 = RecursiveNewtonPolynomial(list(X)[:-1], list(Y)[:-1])
            self.fdd2 = RecursiveNewtonPolynomial(list(X)[1:], list(Y)[1:])

        if error_point:
            x, y = error_point
            self.error_fdd = RecursiveNewtonPolynomial(
                list(X) + [x],
                list(Y) + [y],
            )
        else:
            self.error_fdd = None

    def fdd(self):
        x0 = self.X[0]
        xn = self.X[-1]
        return (self.fdd2.fdd() - self.fdd1.fdd()) / (xn - x0)

    def newton_term_list(self):
        return self.fdd1.newton_term_list() + [self.newton_term()]

    def newton_term(self):
        return lambda xi: self.fdd() * product(xi - xn for xn in self.X)

    def error(self, xi, yi):
        if self.error_fdd is None:
            return None
        else:
            y, _ = self.error_fdd.predict(xi)
            return (y - yi)

    def predict(self, xi):
        y = self.Y[0]
        for term_func in self.newton_term_list():
            y += term_func(xi)
        ea = self.error(xi, y)
        return (y, ea)


class NewtonPolynomial:

    def __init__(self, X, Y):
        assert len(X) > 1, 'Must have two or more data points!'
        assert len(X) == len(Y), 'X and Y arrays must map to each other!'
        self.X = np.array(X, dtype='float64')
        self.Y = np.array(Y, dtype='float64')

    def fit(self):
        X = self.X
        n = len(X)
        fdd = np.zeros((n, n))
        fdd[:, 0] = self.Y.copy()
        for j in range(1, n):
            for i in range(n - j):
                fdd[i, j] = (fdd[i+1, j-1] - fdd[i, j-1]) / (X[i+j] - X[i])
        self.fdd = fdd

    def interpolate(self, xi):
        X = self.X
        fdd = self.fdd
        n = fdd.shape[0]
        y_int = np.zeros((n,), dtype='float64')
        ea = np.zeros((n,), dtype='float64')
        x_term = 1.0
        y_int[0] = fdd[0, 0]
        for order in range(1, n):
            x_term = x_term * (xi - X[order-1])
            y_int2 = y_int[order-1] + fdd[0, order] * x_term
            ea[order-1] = y_int2 - y_int[order-1]
            y_int[order] = y_int2
        return (y_int, ea)
