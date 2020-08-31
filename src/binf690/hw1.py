"""\
Homework 1
Alexander Smith
BINF690 Fall 2020
George Mason University

Problem 1.13

a. Plot V=V(t) and using Euler's algorithm
b. Explain what happens to the droplet at t>10min
c. (Extra) Obtain analytical solution and compare to numeric solution.

"""

import math

import matplotlib.pyplot as plt
import numpy as np


def euler(t_series, y_init, f):
    t_iter = iter(t_series)
    t_prev = next(t_iter)
    y = y_init
    for t_next in t_iter:
        y = y + f(t_prev) * (t_next - t_prev)
        yield y
        t_prev = t_next


def volume(r):
    return (4 * math.pi * r**3) / 3.0


def drdt(t):
    k = -0.08
    return (k * 4 * math.pi * t**2)


def dvdt(t):
    k = -0.08
    return (k * 4 * math.pi * (3 * t / (4 * math.pi))**(2 / 3))


def main():
    t_max = 10
    dt = 0.25
    r_init = 2.5

    t_series = np.arange(0, t_max, dt)
    t_series = np.append(t_series, [t_max])
    print(t_series)

    y = list(euler(t_series, volume(r_init), dvdt))
    t_series = t_series[:len(y)]
    X = np.array([t_series, y])
    # for x1 in X:
    #     print(x1)
    fig, ax = plt.subplots()
    # x = np.array(list(evaporate()))
    # ax.plot(X[:, 0], X[:, 1], label='radius')
    print(X.T)
    ax.plot(X[0, ], X[1, ], label='radius')
    ax.set_xlabel('t (secs)')
    ax.set_ylabel('V(t) (mm^3)')
    ax.set_title('Evaporation')
    plt.savefig('hw1.png')


if __name__ == '__main__':
    main()
