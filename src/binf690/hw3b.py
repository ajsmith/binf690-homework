"""Homework 3: Problem 6.4

Alexander Smith
BINF690
George Mason University
Fall 2020
"""

import matplotlib.pyplot as plt
import numpy as np

from binf690.roots import newton_raphson, newton_raphson_multi


def f(x):
    return -1 + 5.5 * x - 4 * x**2 + 0.5 * x**3


def main():
    # (xr, y) = bisect(dfdx, 0, 1, 0.05, 1000)
    x1 = np.linspace(-1, 7, 1000)

    fig, (ax1, ax2) = plt.subplots(2, 1)

    ax1.plot(x1, f(x1), 'r')
    ax1.plot(0.2, 0, 'mo', label='xr1 ~ 0.2')
    ax1.plot(1.5, 0, 'mo', label='xr2 ~ 1.5')
    ax1.plot(6.3, 0, 'mo', label='xr3 ~ 6.3')
    ax1.axhline(0, color='k', linestyle='--')
    ax1.legend(loc='best')
    # ax2.title('Graphical Method 2')


    # plt.xlabel('x')
    # plt.ylabel('y')
    plt.savefig('hw3b.png')


if __name__ == '__main__':
    main()
