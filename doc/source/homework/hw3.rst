.. Alexander Smith
   BINF690
   George Mason University
   Fall 2020


==========
Homework 3
==========

Solve problems 5.12 and 6.4.


Problem 5.12
============

Given

..  math::

    f(x) = -2x^6 - 1.5x^4 + 10x + 2

Use bisection to find the maximum of this function.

Employ initial guesses of :math:`x_l = 0` and :math:`x_u = 1`, and perform
iterations until the approximate relative error falls below 5%.

The derivative can be used to find the maximum:

..  math::

    f'(x) = -12x^5 - 6x^3 + 10

The roots of the derivative correspond to the minimums and maximums of
the original function.

..  plot::

    import binf690.hw3a
    binf690.hw3a.main()

Graphically, we can see the derivative has a single maximum.


Problem 6.4
===========

Determine the real roots of

..  math::

    f(x) = -1 + 5.5x - 4x^2 + 0.5x^3

(a) Graphically


(b) Using the Newton-Raphson method to within :math:`\epsilon_s = 0.01\%`.

..  plot::

    import binf690.hw3b
    binf690.hw3b.main()
