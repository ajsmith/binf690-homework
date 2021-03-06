.. Alexander Smith
   BINF690
   George Mason University
   Fall 2020


==========
Homework 7
==========


Part A
======

Problem 21.5: Integrate the following function both analytically and
using Simpson's rule, with :math:`n = 4` and :math:`n = 5`.

..  math::

    \int_{-3}^{5} (4x - 3)^3 dx

In addition:

a. compute integral using trapezoidal rule (n=5)
b. compute integral using Romberg integration (n1=5, n2=10)
c. compare numerical results with analytical integration


Solution
--------

..  plot::
    :include-source:

    from binf690.hw7 import plot_hw7a
    plot_hw7a()


Analytical Solution
~~~~~~~~~~~~~~~~~~~

Solving the integral analytically, we find:

..  math::

    \int (4x - 3)^3 dx = \frac{1}{16} (4x - 3)^4

Solving for the definite integral:

..  math::

    \int_{-3}^{5} (4x - 3)^3 dx &= \frac{1}{16} [(4(5)-3)^4 - (4(-3)-3)^4]

                                &= \frac{1}{16} [17^4 - (-15)^4]

                                &= \frac{1}{16} [83521 - 50625]

                                &= \frac{32896}{16}

                                &= \boxed{2056}


Numerical Solutions
~~~~~~~~~~~~~~~~~~~

For full source code, see `hw7.py` and `integration.py` in the
*Implementations* section.

In comparison to the Analytical method, the Simpson and Romberg
methods seem accurate. The Trapezoidal method has significant error
however.

    >>> from binf690.hw7 import simp, trap, romb

Simpson Rule with :math:`n=4`:

    >>> simp(a=-3, b=5, n=4)
    a=-3 b=5 n=4 method=simpson
    result=2056.000

Simpson Rule with :math:`n=5`:

    >>> simp(a=-3, b=5, n=5)
    a=-3 b=5 n=5 method=simpson
    result=2056.000

Trapezoidal Rule with :math:`n=5`:

    >>> trap(a=-3, b=5, n=5)
    a=-3 b=5 n=5 method=trapezoidal
    result=2219.840

Romberg Rule with :math:`n1=5` and :math:`n2=10`:

    >>> romb(a=-3, b=5, n1=5, n2=10)
    a=-3 b=5 n1=5 n2=10 method=romberg
    result=2056.000


Part B
======

Compute the integral for the 3rd order interpolating polynomial from
the derivation of 1/3 Simpson method done in the class.

..  math::

    \int_{0}^{2} \alpha (\alpha - 1) (\alpha - 2) d\alpha = 0


Solution
--------

See attached handwritten proof.
