"""Homework 3: Problem 5.12

Alexander Smith
BINF690
George Mason University
Fall 2020
"""

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return -2 * x**6 - 1.5 * x**4 + 10 * x + 2


def dfdx(x):
    return -12 * x**5 - 6 * x**3 + 10



def bisect(f, xl, xu, es, itermax):
    yl = f(xl)
    xr = xl
    for i in range(itermax):
        xold = xr
        xr = (xl + xu) / 2
        yr = f(xr)
        if xr == 0:
            ea = 1.0
        else:
            ea = abs((xr - xold) / xr)

        # Test the sign and adjust the boundaries
        t = yl * yr
        if t < 0:
            xu = xr
        elif t > 0:
            xl = xr
            yl = yr
        else:
            ea = 0

        if ea < es:
            # Our error is small enough, so we stop early
            break

    return (xr, yr)


def main():
    (xr, y) = bisect(dfdx, 0, 1, 0.05, 1000,)
    x = np.linspace(0, 1, 100)
    plt.plot(x, f(x), 'r', label='f(x)')
    plt.plot(x, dfdx(x), 'b', label='f\'(x)')
    plt.axhline(0, color='k', linestyle='--', label='y=0')
    plt.axvline(xr, color='g', label='xr={}'.format(xr))
    plt.plot(xr, y, 'c.', label='f\'(xr)={}'.format(xr, y))
    plt.plot(xr, f(xr), 'm.', label='f(xr)={}'.format(xr, y))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Problem 5.12')
    plt.legend(loc='best')
    plt.savefig('hw3a.png')


if __name__ == '__main__':
    main()
