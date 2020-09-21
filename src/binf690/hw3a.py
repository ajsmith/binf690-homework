"""Homework 3: Problem 5.12

Alexander Smith
BINF690
George Mason University
Fall 2020
"""

import matplotlib.pyplot as plt
import numpy as np

from binf690.roots import bisect


def f(x):
    return -2 * x**6 - 1.5 * x**4 + 10 * x + 2


def dfdx(x):
    return -12 * x**5 - 6 * x**3 + 10


def main():
    (xr, y) = bisect(dfdx, 0, 1, 0.05, 1000)
    x = np.linspace(0, 1, 100)
    plt.plot(x, f(x), 'r', label='f(x)')
    plt.plot(x, dfdx(x), 'b', label='f\'(x)')
    plt.axhline(0, color='k', linestyle='--', label='y=0')
    plt.axvline(xr, color='k', linestyle=':', label='xr={:.3f}'.format(xr))
    plt.plot(xr, y, 'co', label='f\'(xr)={:.3f}'.format(y))
    plt.plot(xr, f(xr), 'mo', label='f(xr)={:.3f}'.format(f(xr)))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Bisection Method | Ea < 5%')
    plt.legend(loc='best')
    plt.savefig('hw3a.png')


if __name__ == '__main__':
    main()
