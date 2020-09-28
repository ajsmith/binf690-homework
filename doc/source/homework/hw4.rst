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


    >>> import numpy as np
    >>> from binf690.gaussian import gauss_elimination

    >>> m = np.array([
    ...    [8, 2, -2, -2],
    ...    [10, 2, 4, 4],
    ...    [12, 2, 2, 6],
    ... ])
    >>> a = m[:, :-1]
    >>> b = m[:, -1]
    >>> print(a)
    [[ 8  2 -2]
     [10  2  4]
     [12  2  2]]
    >>> print(b)
    [-2  4  6]
    >>> n = a.shape[1]

    >>> x = gauss_elimination(a, b, n)
