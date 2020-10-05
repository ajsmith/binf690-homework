"""Gradient descent optimization.


Alexander Smith
BINF690
George Mason University
Fall 2020
"""

from math import sqrt
from random import random

from binf690.numeric import eps
from binf690.roots import newton_raphson


FDD_DX = 2**(-20)


def gradient_descent(f, dfdx, dfdy, d2fdx2, d2fdy2, d2fdxdy, init=(0, 0)):
    H = Hessian(d2fdx2, d2fdy2, d2fdxdy)
    itermax = 100
    x, y = init
    root_guess = -1
    f0 = 1

    for i in range(itermax):
        if abs(f(x, y) - f0) < eps:
            print(f'Pass {i:2d} x:{x:.3f} y:{y:.3f} h*:{h_star:.3f}')
            print(f'Found optima at x:{x:.3f} y:{y:.3f} h*:{h_star:.3f}')
            break
        xh = x_coord_func(x, y, dfdx)
        yh = y_coord_func(x, y, dfdy)
        g = g_func(f, xh, yh)
        dgdh = centered_fdd_func(g)
        h_star = newton_raphson(g, dgdh, root_guess, 0.01, 1000)
        print(f'Pass {i:2d} x:{x:.3f} y:{y:.3f} h*:{h_star:.3f}')
        x = xh(h_star)
        y = yh(h_star)
        f0 = f(x, y)
        root_guess = (x + y) * random() - (x + y) * random()

    if H(x, y) > 0:
        print('Hessian: {:.3f}'.format(H(x, y)))
        if d2fdx2(x, y) > 0:
            print('Has local minimum')
        elif d2fdx2(x, y) < 0:
            print('Has local maximum')
    elif H(x, y) < 0:
        raise ValueError('Saddlepoint')
    else:
        raise ValueError('Undefined Hessian')


def x_coord_func(x0, y0, dfdx):
    return lambda h: x0 + h * dfdx(x0, y0)


def y_coord_func(x0, y0, dfdy):
    return lambda h: y0 + h * dfdy(x0, y0)


def g_func(f, xh, yh):
    return lambda h: f(xh(h), yh(h))


def centered_fdd_func(f, dx=FDD_DX):
    return lambda x: (f(x + dx) - f(x - dx)) / (2 * dx)


class Hessian:

    def __init__(self, d2fdx2, d2fdy2, d2fdxdy):
        self.d2fdx2 = d2fdx2
        self.d2fdy2 = d2fdy2
        self.d2fdxdy = d2fdxdy

    def __call__(self, x, y):
        return self.d2fdx2(x, y) * self.d2fdy2(x, y) - self.d2fdxdy(x, y)**2
