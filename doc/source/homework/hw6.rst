.. Alexander Smith
   BINF690
   George Mason University
   Fall 2020


==========
Homework 6
==========


Problem 17.6
============


Solution
--------

The linear regression of the given data set fits the line:

..  math::

    y = -2.014 + 1.458x

See `hw6.py` and `regression.py` in the *Implementations* section for
full source code.

    >>> from binf690.hw6 import hw6a
    >>> hw6a()
    X: 1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0
    Y: 1.0 1.5 2.0 3.0 4.0 5.0 8.0 10.0 13.0
    Linear Regression:
    a0:-2.014  a1:1.458  R:0.956  Std. Error:1.307
    Polynomial Regression:
    a0:1.488  a1:-0.452  a2:0.191  R:0.997  Std. Error:0.345

..  plot::

    from binf690.hw6 import hw6a_plot
    hw6a_plot()


Problem 18.5
============

- Predict the value of the function at :math:`x = 2.8`.
- Use fifth order interpolating polynomial.


Solution
--------

Answers to problem below. See `hw6.py` and `interpolation.py` in the
*Implementations* section for full source.

import pdb; pdb.set_trace();

    >>> from binf690.hw6 import hw6b
    >>> hw6b()
    X: 1.6 2.0 2.5 3.2 4.0 4.5
    Y: 2.0 8.0 14.0 15.0 8.0 2.0
    Order Polynomial: 5
    f(2.8) ~= 19.803

..  plot::

    from binf690.hw6 import hw6b_plot
    hw6b_plot()
