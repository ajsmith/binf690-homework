"""Homework 6

Alexander Smith
BINF690
George Mason University
Fall 2020

"""

import matplotlib.pyplot as plt
import numpy as np

from binf690.regression import LinearRegression, PolynomialRegression


class Homework6A:

    def __init__(self, X=None, Y=None):
        self.X = X or [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.Y = Y or [1, 1.5, 2, 3, 4, 5, 8, 10, 13]
        self.linear = LinearRegression(self.X, self.Y)
        self.poly = PolynomialRegression(2, self.X, self.Y)

    def print_solution(self):
        print('X:', ' '.join(f'{x:2.1f}' for x in self.X))
        print('Y:', ' '.join(f'{y:2.1f}' for y in self.Y))
        print('Linear Regression:')
        print(self.linear)
        print('Polynomial Regression:')
        print(self.poly)


def hw6a():
    hw = Homework6A()
    hw.print_solution()


def hw6a_plot():
    hw = Homework6A()
    X = np.array(hw.X, dtype='float64')
    Y = np.array(hw.Y, dtype='float64')
    plt.scatter(X, Y, c='k')
    plt.plot(X, hw.linear.predict(X), 'b', label='Linear')
    plt.plot(X, hw.poly.predict(X), 'r', label='Polynomial')
    plt.legend(loc='best')
    plt.savefig('asmitl-hw6a.png')


def hw6b():
    not_yet


if __name__ == '__main__':
    hw6a_plot()
#    hw6b()
