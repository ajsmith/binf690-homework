"""Homework 6

Alexander Smith
BINF690
George Mason University
Fall 2020

"""

import matplotlib.pyplot as plt
import numpy as np

from binf690.interpolation import NewtonPolynomial, RecursiveNewtonPolynomial
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


class Homework6B:

    def __init__(self, X=None, Y=None):
        self.X = X or [1.6, 2, 2.5, 3.2, 4, 4.5]
        self.Y = Y or [2, 8, 14, 15, 8, 2]
        # self.X = X or [1.6, 2, 2.5, 3.2, 4]
        # self.Y = Y or [2, 8, 14, 15, 8]
        # self.error_point = (4.5, 2)
        self.newton = RecursiveNewtonPolynomial(self.X, self.Y)


    def print_solution(self):
        yn, ea = self.newton.predict(2.8)
        print('X:', ' '.join(f'{x:.1f}' for x in self.X))
        print('Y:', ' '.join(f'{y:.1f}' for y in self.Y))
        # print(f'Error Point: {self.error_point}')
        print(f'Order Polynomial: {self.newton.order}')
        print(f'f(2.8) ~= {yn:.3f}')
        # print(f'Error: {ea:.3f}')


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
    plt.show()
    plt.savefig('asmitl-hw6a.png')


def hw6b():
    hw = Homework6B()
    hw.print_solution()


def hw6b_plot():
    hw = Homework6B()
    X = np.array(hw.X, dtype='float64')
    Y = np.array(hw.Y, dtype='float64')
    plt.scatter(X, Y, c='k')
    plt.show()
    plt.savefig('asmitl-hw6b.png')


if __name__ == '__main__':
    hw6a_plot()
    hw6b_plot()
