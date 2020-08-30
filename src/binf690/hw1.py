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


def euler(t2, t1, f):
    p = f(t2) - f(t1)
    q = t2 - t1
    return (p / q)


def volume(r):
    return (4 * math.pi * r**3) / 3.0


def evaporate():
    t = 0
    dt = 0.25
    t_max = 10.1
    k = 0.08
    r = 2.5
    while t < t_max:
        yield (t, volume(r))
        r = r + (-k * (4 * math.pi * r**2) * dt)
        t += dt


def main():
    # t = 0
    # dt = 15
    # t_max = 60 * 10
    # ts = list(range(t, t_max, dt))
    # xs = (euler(t, dt))
    fig, ax = plt.subplots()
    x = np.array(list(evaporate()))
    ax.plot(x[:,0], x[:,1])
    ax.set_xlabel('t (secs)')
    ax.set_ylabel('V(t) (mm^3)')
    ax.set_title('Evaporation')
    plt.savefig('hw1.png')


if __name__ == '__main__':
    main()
