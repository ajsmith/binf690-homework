"""Homework 3: Problem 6.4

Alexander Smith
BINF690
George Mason University
Fall 2020
"""

import matplotlib.pyplot as plt
import numpy as np

from binf690.roots import newton_raphson


def f(x):
    return -1 + 5.5 * x - 4 * x**2 + 0.5 * x**3


def dfdx1(x):
    return 5.5 - 8 * x + 1.5 * x**2


def main():
    x1 = np.linspace(-1, 7, 1000)

    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle('Graphical and Newton-Raphson Methods')

    ax1.plot(x1, f(x1), 'r')
    ax1.plot(0.2, 0, 'mo', label='xr1 ~ 0.2')
    ax1.plot(1.5, 0, 'mo', label='xr2 ~ 1.5')
    ax1.plot(6.3, 0, 'mo', label='xr3 ~ 6.3')
    ax1.axhline(0, color='k', linestyle='--')
    ax1.set_ylabel('Graphical')
    ax1.legend(loc='best')

    xr1, xr2, xr3 = [
        newton_raphson(f, dfdx1, x, 0.01, 1000)
        for x in (0.2, 1.5, 6.3)
    ]
    ax2.plot(x1, f(x1), 'r')
    ax2.plot(xr1, 0, 'co', label=f'xr1 = {xr1:.3f}')
    ax2.plot(xr2, 0, 'co', label=f'xr2 = {xr2:.3f}')
    ax2.plot(xr3, 0, 'co', label=f'xr3 = {xr3:.3f}')
    ax2.axhline(0, color='k', linestyle='--')
    ax2.set_ylabel('Newton-Raphson')
    ax2.legend(loc='best')

    plt.savefig('hw3b.png')


if __name__ == '__main__':
    main()
