"""Linear regression implementation.

Alexander Smith
BINF690
George Mason University
Fall 2020

"""

from collections import namedtuple
from math import sqrt

import matplotlib.pyplot as plt
import numpy as np


class LinearRegression:

    def __init__(self, X, Y):
        assert len(X) > 1, 'Must have at least three data points!'
        assert len(X) == len(Y), 'X and Y arrays must map to each other!'
        self.X = X
        self.Y = Y
        self.fit()

    def fit(self):
        n = len(self.X)
        x_sum = sum(self.X)
        y_sum = sum(self.Y)
        xy_sum = sum(x*y for (x, y) in zip(self.X, self.Y))
        x2_sum = sum(x**2 for x in self.X)
        x_avg = x_sum / len(self.X)
        y_avg = y_sum / len(self.Y)
        a1 = (n * xy_sum - x_sum * y_sum) / (n * x2_sum - x_sum**2)
        a0 = y_avg - x_avg * a1
        St = sum((y - y_avg)**2 for y in self.Y)
        Sr = sum((y - a0 - a1 * x)**2 for (x, y) in zip(self.X, self.Y))
        R = sqrt((St - Sr) / St)
        std_error = sqrt(Sr / (n - 2))
        self.a1 = a1
        self.a0 = a0
        self.St = St
        self.Sr = Sr
        self.R = R
        self.std_error = std_error

    def predict(self, x):
        return self.a0 + self.a1 * x

    def plot(self, filename=None):
        X = np.array(self.X)
        Y = np.array(self.Y)
        plt.scatter(X, Y)
        plt.plot(X, self.predict(X), 'r')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()
        if filename:
            plt.savefig(filename)

    def __str__(self):
        return (
            f'a0:{self.a0:.3f}'
            f'  a1:{self.a1:.3f}'
            f'  R:{self.R:.3f}'
            f'  Std. Error:{self.std_error:.3f}'
        )
