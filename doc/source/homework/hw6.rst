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

..  plot::

    from binf690.hw6 import hw6a_plot
    hw6a_plot()


Problem 18.5
============

- Predict the value of the function at :math:`x = 2.8`.
- Use fifth order interpolating polynomial.
