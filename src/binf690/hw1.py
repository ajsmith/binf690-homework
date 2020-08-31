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
    yield y
    for t_next in t_iter:
        y = y + f(y) * (t_next - t_prev)
        yield y
        t_prev = t_next


def time_series(t_final, dt, t_init=0):
    t_series = np.arange(t_init, t_final, dt)
    return np.append(t_series, [t_final])


def volume(r):
    return (4 * math.pi * r**3) / 3.0


def v_to_r(v):
    return (3 * v / (4 * math.pi))**(1/3)


def dvdt(v):
    k = -0.08
    return (k * 4 * math.pi * v_to_r(v)**2)


def main():
    t_final = 10
    dt = 0.25
    v_init = volume(2.5)

    t_series = time_series(t_final, dt)
    y = list(euler(t_series, v_init, dvdt))
    r = v_to_r(np.array(y))
    X = np.array([t_series, y, r])
    print(X.T)

    fig, ax = plt.subplots()
    ax.plot(X[0, ], X[1, ], label='Volume')
    # ax.plot(X[0, ], X[2, ], label='Radius')
    ax.set_xlabel('t (min)')
    ax.set_ylabel('V(t) (mm^3)')
    ax.set_title('Evaporation')
    ax.text(1, 20, 'At t>10min, V(t) asymptotically approaches zero')
    plt.savefig('asmitl-hw1.png')


if __name__ == '__main__':
    main()
