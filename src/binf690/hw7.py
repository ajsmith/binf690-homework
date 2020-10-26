"""Homework 6

Alexander Smith
BINF690
George Mason University
Fall 2020

"""

import matplotlib.pyplot as plt
import numpy as np

from binf690.integration import integral, romberg


def f(x):
    return (4 * x - 3)**3


def plot_hw7a(filename=None):
    x1 = np.linspace(-5, 7, 100)
    plt.plot(x1, f(x1), label='f(x)')
    plt.axhline(0, color='k', linestyle='-', label='x=-3')
    plt.axvline(-3, color='k', linestyle=':', label='x=-3')
    plt.axvline(5, color='k', linestyle=':', label='x=5')
    x2 = np.linspace(-3, 5, 100)
    plt.fill_between(x2, f(x2), color='c')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(r'$\int_{-3}^{5} (4x - 3)^3 dx$')
    if filename:
        plt.savefig(filename)


def print_result(a, b, n, method, result):
    print(f'a={a} b={b} n={n} method={method}')
    print(f'result={result:.3f}')


def simp(f=f, a=0, b=1, n=1):
    method = 'simpson'
    result = integral(f, a, b, n, method=method)
    print_result(a, b, n, method, result)


def trap(f=f, a=0, b=1, n=1):
    method = 'trapezoidal'
    result = integral(f, a, b, n, method=method)
    print_result(a, b, n, method, result)


def romb(f=f, a=0, b=1, n1=1, n2=2):
    result = romberg(f, a, b, n1, n2)
    print(f'a={a} b={b} n1={n1} n2={n2} method=romberg')
    print(f'result={result:.3f}')
