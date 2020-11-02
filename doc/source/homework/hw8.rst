.. Alexander Smith
   BINF690
   George Mason University
   Fall 2020


==========
Homework 8
==========


Problem 25.5
============

Solve from :math:`t = 0` to 3 with :math:`h = 0.1` using:

a. Heun (without corrector)
b. Ralston's second-order RK method

..  math::

    \frac{dy}{dt} = y \sin^3 (t) \qquad y(0) = 1

Please note that Heun (or predictor-corrector method) without
corrector is an Euler method.

In addition:

1. Use predictor-corrector method
2. Use 4th order RK method
3. Plot all solutions


Solution
========

For full source code, see `hw8.py` and `ode.py` in the
*Implementations* section.

..  plot::
    :include-source:

    >>> from binf690.hw8 import plot_all
    >>> plot_all()


Heun without corrector
----------------------

    >>> from binf690.hw8 import solve_euler
    >>> solve_euler()
    i:  0  x: 0.0  y: 1.000  h: 0.0
    i: 10  x: 1.0  y: 1.159  h: 0.1
    i: 20  x: 2.0  y: 2.668  h: 0.1
    i: 30  x: 3.0  y: 3.620  h: 0.1

..  plot::
    :include-source:

    >>> from binf690.hw8 import plot_euler
    >>> plot_euler()


Heun with corrector
-------------------

    >>> from binf690.hw8 import solve_heun
    >>> solve_heun()
    i:  0  x: 0.0  y: 1.000  h: 0.0
    i: 10  x: 1.0  y: 1.197  h: 0.1
    i: 20  x: 2.0  y: 2.877  h: 0.1
    i: 30  x: 3.0  y: 3.788  h: 0.1

..  plot::
    :include-source:

    >>> from binf690.hw8 import plot_heun
    >>> plot_heun()


Ralston's 2nd Order RK Method
-----------------------------

    >>> from binf690.hw8 import solve_ralston
    >>> solve_ralston()
    i:  0  x: 0.0  y: 1.000  h: 0.0
    i: 10  x: 1.0  y: 1.196  h: 0.1
    i: 20  x: 2.0  y: 2.878  h: 0.1
    i: 30  x: 3.0  y: 3.788  h: 0.1

..  plot::
    :include-source:

    >>> from binf690.hw8 import plot_ralston
    >>> plot_ralston()


4th Order RK Method
-------------------

    >>> from binf690.hw8 import solve_rkm4
    >>> solve_rkm4()
    i:  0  x: 0.0  y: 1.000  h: 0.0
    i: 10  x: 1.0  y: 1.196  h: 0.1
    i: 20  x: 2.0  y: 2.883  h: 0.1
    i: 30  x: 3.0  y: 3.793  h: 0.1

..  plot::
    :include-source:

    >>> from binf690.hw8 import plot_rkm4
    >>> plot_rkm4()
