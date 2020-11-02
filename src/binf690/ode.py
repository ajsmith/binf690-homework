"""Methods to approximate ordinary differential equations.

Alexander Smith
BINF690
George Mason University
Fall 2020

"""

import numpy as np


def series(t_init, t_final, dt):
    """Return a series on [t_init, t_final] with an interval of dt."""
    assert t_init < t_final
    assert dt > 0
    result = np.arange(t_init, t_final, dt)
    result = np.append(result, [t_final])
    return result


def euler(dxdy, x, y, h):
    """Euler method."""
    return y + dxdy(x, y) * h


def heun(dxdy, x, y, h):
    """Heun predictor-corrector method."""
    m1 = dxdy(x, y)
    m2 = dxdy(x + h, y + m1 * h)
    return y + ((m1 + m2) / 2.0) * h


def ralston(dxdy, x, y, h):
    """Ralston 2nd order Runge-Kutta method."""
    k1 = dxdy(x, y)
    k2 = dxdy(x + h * 3.0 / 4, y + k1 * h * 3.0 / 4)
    return y + (k1 / 3.0 + k2 * 2 / 3.0) * h


def rkm4(dxdy, x, y, h):
    """Classical 4th order Runge-Kutta method."""
    k1 = dxdy(x, y)
    k2 = dxdy(x + h / 2.0, y + k1 * h / 2.0)
    k3 = dxdy(x + h / 2.0, y + k2 * h / 2.0)
    k4 = dxdy(x + h, y + k3 * h)
    return y + (k1 + 2 * k2 + 2 * k3 + k4) * h / 6.0


def solve(method, dxdy, yi=0, xi=0, xf=1, dx=1):
    """Approximate a solution for dxdy."""
    xs = series(xi, xf, dx)
    i = 0
    yield (i, xi, yi, 0)
    for x in xs[1:]:
        i += 1
        h = x - xi
        y = method(dxdy, xi, yi, h)
        yield (i, x, y, h)
        xi, yi = x, y
