"""Methods for approximating solutions of integrations.

Alexander Smith
BINF690
George Mason University
Fall 2020

"""

import numpy as np


def calc_h(a, b, n):
    return float(b - a) / n


def trapezoidal_single(h, y1, y2):
    return h * (y2 + y1) / 2.0


def trapezoidal(y, h):
    """Return the integral of a function using Trapezoidal method."""
    assert len(y) > 1, 'Need at least two points!'
    result = y[0] + y[-1]
    result += 2 * sum(y[1:-1])
    result *= h / 2.0
    return result


def romberg(y, h1, h2):
    """Return the integral of a function using Romberg method."""
    not_yet


def simpson38(y, h):
    y0, y1, y2, y3 = y
    return 3 * h * (y0 + 3 * y1 + 3 * y2 + y3) / 8.0


def simpson13(y, h):
    result = y[0]
    result += sum(4 * y1 + 2 * y2 for (y1, y2) in pairs(y[1:-2]))
    result += 4 * y[-2] + 2 * y[-1]
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


def simpson(y, h):
    """Return the integral of a function using Simpson method."""
    n = len(y) - 1
    result = 0
    if n == 1:
        result = trapezoidal_multi(y, h)
    elif n > 1:
        if is_odd(n):
            result = simpson38(y[:4], h)
            y = y[4:]
        if y:
            result += simpson13(y, h)
    return result


def integration_methods():
    return {
        'trapezoidal': trapezoidal,
        'simpson': simpson,
        'romberg': romberg,
    }


def integral(f, a, b, n, method='simpson'):
    int_methods = integration_methods()
    assert method in int_methods, f'Unknown integral method: {method}'
    int_func = int_methods[method]

    h = calc_h(a, b, n)
    x = range(n + 1)
    y = [f(xi) for xi in x]
    result = int_func(y, h)
    return (result, h)
