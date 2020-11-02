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


def solve_heun():
    result = solve(heun, dydt, **initial_args)
    display_results(result)


def solve_ralston():
    result = solve(ralston, dydt, **initial_args)
    display_results(result)


def solve_rkm4():
    result = solve(rkm4, dydt, **initial_args)
    display_results(result)


def get_plot_vars(result):
    result = list(result)
    xs = list(x for (_, x, _, _) in result)
    ys = list(y for (_, _, y, _) in result)
    return xs, ys


def plot_all(filename=None):
    euler_result = solve(euler, dydt, **initial_args)
    heun_result = solve(heun, dydt, **initial_args)
    ralston_result = solve(ralston, dydt, **initial_args)
    rkm4_result = solve(rkm4, dydt, **initial_args)

    xs, y_euler = get_plot_vars(euler_result)
    _, y_heun = get_plot_vars(heun_result)
    _, y_ralston = get_plot_vars(ralston_result)
    _, y_rkm4 = get_plot_vars(rkm4_result)

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


def plot_2x2(filename=None):
    euler_result = solve(euler, dydt, **initial_args)
    heun_result = solve(heun, dydt, **initial_args)
    ralston_result = solve(ralston, dydt, **initial_args)
    rkm4_result = solve(rkm4, dydt, **initial_args)

    xs, y_euler = get_plot_vars(euler_result)
    _, y_heun = get_plot_vars(heun_result)
    _, y_ralston = get_plot_vars(ralston_result)
    _, y_rkm4 = get_plot_vars(rkm4_result)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle(r'$\frac{dy}{dt} = y \sin^3 (t) \qquad y(0) = 1$')

    ax1.plot(xs, y_euler, 'b-o', ms=3)
    ax1.set_ylabel('Heun w/o Corrector')
    ax1.axhline(
        y_euler[-1], c='m', ls='-', label=f'y = {y_euler[-1]:.3f}')

    ax2.plot(xs, y_heun, 'b-o', ms=3)
    ax2.set_ylabel('Heun w/ Corrector')
    ax2.axhline(
        y_heun[-1], c='m', ls='-', label=f'y = {y_heun[-1]:.3f}')

    ax3.plot(xs, y_ralston, 'b-o', ms=3)
    ax3.set_ylabel('Ralston 2nd Order RKM')
    ax3.axhline(
        y_ralston[-1], c='m', ls='-', label=f'y = {y_ralston[-1]:.3f}')

    ax4.plot(xs, y_rkm4, 'b-o', ms=3)
    ax4.set_ylabel('4th Order RKM')
    ax4.axhline(
        y_rkm4[-1], c='m', ls='-', label=f'y = {y_rkm4[-1]:.3f}')

    for ax in (ax1, ax2, ax3, ax4):
        ax.grid(color='k', ls=':', lw=0.1)
        ax.legend(loc='best')

    if filename:
        plt.savefig(filename)


if __name__ == '__main__':
    plot_all('asmitl-hw8-all.png')
    plot_all2('asmitl-hw8-2x2.png')
