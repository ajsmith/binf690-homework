"""Methods to approximate systems of ordinary differential equations.

Alexander Smith
BINF690
George Mason University
Fall 2020

"""

import matplotlib.pyplot as plt
import numpy as np


def series(t_init, t_final, dt):
    """Return a series on [t_init, t_final] with an interval of dt."""
    assert t_init < t_final
    assert dt > 0
    result = np.arange(t_init, t_final, dt)
    result = np.append(result, [t_final])
    return result


def euler(dydx, xi, yi, yi_vec, h):
    """Euler method."""
    return yi + dydx(xi, *yi_vec) * h


METHODS = {
    'euler': euler,
}


def compute(ode_vec, yi_vec, xi=0, xf=1, dx=1, method='euler'):
    xs = series(xi, xf, dx)
    method = METHODS.get(method, euler)
    i = 0
    yield (i, xi, yi_vec, 0)
    for x in xs[1:]:
        i += 1
        h = x - xi
        y_vec = []
        for (j, dydt) in enumerate(ode_vec):
            y = method(dxdy, xi, yi_vec[j], yi_vec, h)
            y_vec.append(y)
        yield (i, x, y_vec, h)
        xi, yi_vec = x, y_vec


def solve(ode_vec, yi_vec, xi=0, xf=1, dx=1, method='euler'):
    """Approximate a solution for dxdy."""
    assert len(ode_vec) == len(yi_vec), "Each ODE requires an initial value!"

    xs = series(xi, xf, dx)
    method = METHODS.get(method, euler)
    i_vec = [0]
    h_vec = [0]
    x_vec = [xi]
    y_mat = [[yi] for yi in yi_vec]

    for (i, x) in enumerate(xs[1:], 1):
        h = x - xi
        i_vec.append(i)
        x_vec.append(x)
        h_vec.append(h)
        y_tmp = []
        for (j, dydt) in enumerate(ode_vec):
            y = method(dydt, xi, yi_vec[j], yi_vec, h)
            y_tmp.append(y)
            y_mat[j].append(y)
        xi, yi_vec = x, y_tmp

    return (i_vec, h_vec, x_vec, y_mat)


def draw(*args, filename=None, **kwargs):
    """Approximate a solution for dxdy and draw it."""
    solutions = solve(*args, **kwargs)
    x = solutions[2]
    ys = solutions[3]
    fig, ax = plt.subplots()
    for (i, y) in enumerate(ys, 1):
        ax.plot(x, y, label=f'y{i}(t)')
    ax.legend(loc='best')
    if filename:
        fig.savefig(filename)


def demo():
    dy1 = lambda x, y1, y2, y3: -0.5 * y2
    dy2 = lambda x, y1, y2, y3: y1
    dy3 = lambda x, y1, y2, y3: y2 - y1
    ode_vec = [dy1, dy2, dy3]
    yi_vec = [1, 0, 3]
    xi = 0
    xf = 10
    dx = 0.1
    output_file = 'ode-system.png'
    draw(ode_vec, yi_vec, xi, xf, dx, filename=output_file)
