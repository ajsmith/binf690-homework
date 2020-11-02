"""Homework 8

Alexander Smith
BINF690
George Mason University
Fall 2020

"""

from math import sin

import matplotlib.pyplot as plt

from binf690.ode import solve, euler, heun, ralston, rkm4
from binf690.numeric import is_int


initial_args = {
    'yi': 1,
    'xi': 0,
    'xf': 3,
    'dx': 0.1,
}


def dydt(t, y):
    return y * sin(t)**3


def display_results(result, filtering=True):
    if filtering:
        result = filter(lambda row: is_int(row[1]), result)

    for (i, x, y, h) in result:
        print(f'i: {i:2d}  x: {x:.1f}  y: {y:.3f}  h: {h:.1f}')


def solve_euler():
    result = solve(euler, dydt, **initial_args)
    display_results(result)


def plot_euler(filename=None):
    result = solve(euler, dydt, **initial_args)
    _plot(result, 'Heun without corrector', filename)


def solve_heun():
    result = solve(heun, dydt, **initial_args)
    display_results(result)


def plot_heun(filename=None):
    result = solve(heun, dydt, **initial_args)
    _plot(result, 'Heun with corrector', filename)


def solve_ralston():
    result = solve(ralston, dydt, **initial_args)
    display_results(result)


def plot_ralston(filename=None):
    result = solve(ralston, dydt, **initial_args)
    _plot(result, 'Ralston 2nd Order Runge-Kutta Method', filename)


def solve_rkm4():
    result = solve(rkm4, dydt, **initial_args)
    display_results(result)


def plot_rkm4(filename=None):
    result = solve(rkm4, dydt, **initial_args)
    _plot(result, 'Classical 4th Order Runge-Kutta Method', filename)


def _plot(result, title, filename=None):
    result = list(result)
    xs = list(x for (_, x, y, _) in result)
    ys = list(y for (_, x, y, _) in result)

    plt.plot(xs, ys, 'b-o', ms=3, label='f(t)')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title(title)

    if filename:
        plt.savefig(filename)


def plot_all(filename=None):
    euler_result = solve(euler, dydt, **initial_args)
    heun_result = solve(heun, dydt, **initial_args)
    ralston_result = solve(ralston, dydt, **initial_args)
    rkm4_result = solve(rkm4, dydt, **initial_args)

    euler_result = list(euler_result)
    xs = list(x for (_, x, _, _) in euler_result)
    y_euler = list(y for (_, _, y, _) in euler_result)
    y_heun = list(y for (_, _, y, _) in heun_result)
    y_ralston = list(y for (_, _, y, _) in ralston_result)
    y_rkm4 = list(y for (_, _, y, _) in rkm4_result)

    plt.plot(xs, y_euler, 'b-o', ms=3, label='Heun w/o Corrector')
    plt.plot(xs, y_heun, 'r-o', ms=3, label='Heun w/ Corrector')
    plt.plot(xs, y_ralston, 'g-o', ms=3, label='Ralston 2nd Order RKM')
    plt.plot(xs, y_rkm4, 'm-o', ms=3, label='4th Order RKM')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title(r'$\frac{dy}{dt} = y \sin^3 (t) \qquad y(0) = 1$')
    plt.legend(loc='best')

    if filename:
        plt.savefig(filename)


if __name__ == '__main__':
    plot_all('asmitl-hw8-all.png')
