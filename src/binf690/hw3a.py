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


def main():
    x = np.linspace(0, 1, 100)
    plt.plot(x, f(x), 'r', label='f(x)')
    plt.plot(x, dfdx(x), 'b', label='f\'(x)')
    plt.axhline(0, color='k', linestyle='--', label='y=0')
    plt.axvline(0.9, color='g', label='xr')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Problem 5.12')
    plt.legend(loc='best')
    plt.savefig('hw3a.png')
