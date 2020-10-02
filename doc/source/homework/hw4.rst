.. Alexander Smith
   BINF690
   George Mason University
   Fall 2020


==========
Homework 4
==========

Solve problem 9.9.


Problem 9.9
===========

Use Gauss elimination to solve:

..  math::

    8x_1 + 2x_2 - 2x_3 = -2

    10x_1 + 2x_2 + 4x_3 = 4

    12x_1 + 2x_2 + 2x_3 = 6

Employ partial pivoting and check your answers by subsituting them
into the original equations.


Solution
========

Below is Python code demonstrating the solution. The source code for
Gaussian Elimination, `gaussian.py`, can be found in the
*Implementations* section. This solution uses the `NumPy` library for
a matrix implementation.

    >>> import numpy as np
    >>> from binf690.gaussian import gauss_elimination

    >>> m = np.array([
    ...    [8, 2, -2, -2],
    ...    [10, 2, 4, 4],
    ...    [12, 2, 2, 6],
    ... ], dtype='float64')
    >>> a = m[:, :-1].copy()
    >>> b = m[:, -1].copy()
    >>> print(a)
    [[ 8.  2. -2.]
     [10.  2.  4.]
     [12.  2.  2.]]
    >>> print(b)
    [-2.  4.  6.]
    >>> n = a.shape[1]

    >>> x = gauss_elimination(a, b, n)
    >>> print(x)
    [ 1.5 -6.5  0.5]
    >>> print(a)
    [[ 8.  2. -2.]
     [ 0. -1.  5.]
     [ 0.  0.  4.]]
    >>> print(b)
    [-2.  9.  2.]
    >>> (np.matmul(m[:, :-1], x) == m[:, -1]).all()
    True
    >>> np.matmul(m[:, :-1], x)
    array([-2.,  4.,  6.])
