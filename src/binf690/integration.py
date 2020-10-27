"""Methods for approximating solutions of integrations.

Alexander Smith
BINF690
George Mason University
Fall 2020

"""

import numpy as np


def sample_space(a, b, n):
    return np.linspace(a, b, n + 1)


def calc_h(a, b, n):
    return float(b - a) / n


def setup_vars(a, b, n):
    x = sample_space(a, b, n)
    h = calc_h(a, b, n)
    return (x, h)


def trapezoidal_single(h, y1, y2):
    return h * (y2 + y1) / 2.0


def trapezoidal(f, a, b, n):
    """Return the integral of a function using Trapezoidal method."""
    x, h = setup_vars(a, b, n)
    y = [f(xi) for xi in x]
    result = y[0] + y[-1]
    result += 2 * sum(y[1:-1])
    result *= h / 2.0
    return result


def romberg(f, a, b, n1, n2):
    """Return the integral of a function using Romberg method."""
    h1 = calc_h(a, b, n1)
    h2 = calc_h(a, b, n2)
    i1 = trapezoidal(f, a, b, n1)
    i2 = trapezoidal(f, a, b, n2)
    result = i2 + (i2 - i1) / ((h1 / h2)**2 - 1)
    return result


def simpson38(f, x, h):
    y0, y1, y2, y3 = [f(xi) for xi in x]
    return 3 * h * (y0 + 3 * y1 + 3 * y2 + y3) / 8.0


def simpson13(f, x, h):
    y = [f(xi) for xi in x]
    result = y[0]
    result += sum(4 * y1 + 2 * y2 for (y1, y2) in pairs(y[1:-2]))
    result += 4 * y[-2] + y[-1]
    result = h * result / 3.0
    return result


def is_odd(n):
    """Return True if n is an odd number."""
    n = abs(n)
    assert n - int(n) == 0, 'n must be an integer!'
    n = n / 2.0 - int(n / 2.0)
    return (n > 0)


def pairs(x):
    """Yield the items in a list grouped as pairs."""
    it = iter(x)
    while True:
        try:
            yield (next(it), next(it))
        except StopIteration:
            break


def simpson(f, a, b, n):
    """Return the integral of a function using Simpson method."""
    result = 0
    if n == 1:
        result = trapezoidal(f, a, b, n)
    elif n > 1:
        x, h = setup_vars(a, b, n)
        if is_odd(n):
            result = simpson38(f, x[:4], h)
            x = x[3:]
        if len(x) > 0:
            result += simpson13(f, x, h)
    return result
