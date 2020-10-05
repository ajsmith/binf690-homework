.. Alexander Smith
   BINF690
   George Mason University
   Fall 2020


==========
Homework 5
==========



Problem 14.8
============

Locate the minimum of:

..  math::

    f(x, y) = -8x + x^2 + 12y + 4y^2 - 2xy

Using initial guesses:

..  math::
    x = 0

    y = 0


Solution
--------

Partial derivatives with respect to :math:`x` and :math:`y`.

..  math::
    \frac{\partial f}{\partial x} &= -8 + 2x - 2y

    \frac{\partial f}{\partial y} &= 12 + 8y - 2x

    \frac{\partial^2 f}{\partial x^2} &= 2

    \frac{\partial^2 f}{\partial y^2} &= 8

    \frac{\partial^2 f}{\partial x \partial y} &= -2

Now the numeric solution. See `hw5.py` and `gradient.py` in the
*Implementations* section for full source code and implementation

    >>> from binf690.hw5 import hw5
    >>> hw5()
    Pass  0 x:0.000 y:0.000 h*:-0.250
    Pass  1 x:2.000 y:-3.000 h*:-0.250
    Found optima at x:2.000 y:-3.000 h*:-0.250
    Has local minimum
