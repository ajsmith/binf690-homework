=============
Interpolation
=============

The general form of Newton's Interpolating Polynomials is a recursive
application of the finite divided difference.

In these examples, we'll attempt to approximate the natural logarithm
of 2.

    >>> from math import log
    >>> true_value = log(2)
    >>> true_value
    0.6931471805599453

First, we start with a 1st order finite divided difference and
starting points x0=1 and x1z=6.

    >>> from binf690.interpolation import FDD
    >>> p0 = (1, 0)
    >>> p2 = (6, 1.791759)
    >>> fdd = FDD(p0, p2)

An FDD has a slope.

    >>> fdd.slope()
    0.3583518

An FDD can calculate a linear approximation of :math:`f(x)`, in this
case :math:`x = 2`.

    >>> fdd(2)
    0.3583518

Our error is around 48%.

    >>> from binf690.numeric import relative_true_error
    >>> relative_true_error(true_value, fdd(2))
    0.48300763524636636

Then choose a closer point to get a better approximation.

    >>> p1 = (4, 1.386294)
    >>> fdd = FDD(p0, p1)
    >>> fdd.slope()
    0.46209799999999995
    >>> fdd(2)
    0.46209799999999995

Our error is now closer to 33%.

    >>> relative_true_error(true_value, fdd(2))
    0.33333350699529185

Trivially, we can calculate the same linear slope and approximation
using a recursive FDD implementation.

    >>> from binf690.interpolation import RecursiveFDD
    >>> fdd = RecursiveFDD([p0, p1])
    >>> fdd.slope()
    0.46209799999999995
    >>> fdd(2)
    0.46209799999999995

Recursive FDDs also require a minimum two points, the requirement for
a 1st order FDD.

    >>> RecursiveFDD([])
    Traceback (most recent call last):
    ValueError: At least 2 points needed!
    >>> RecursiveFDD([p0])
    Traceback (most recent call last):
    ValueError: At least 2 points needed!

More interestingly, we can create a 2nd-order FDD, which can provide
an even more accurate estimate. This has an error of 18%.

    >>> fdd = RecursiveFDD([p0, p1, p2])
    >>> fdd.slope()
    -0.05187309999999997
    >>> fdd(2)
    0.5658441999999999
    >>> relative_true_error(true_value, fdd(2))
    0.1836593787442173

We can add yet another point to further improve our approximation. Now
the error is 9%.

    >>> p3 = (5, 1.609438)
    >>> fdd = RecursiveFDD([p0, p1, p2, p3])
    >>> fdd.slope()
    0.007865400000000014
    >>> fdd(2)
    0.6287674
    >>> relative_true_error(true_value, fdd(2))
    0.09288039014735279

A RecursiveFDD is able to approximate its error if given an extra data
point. Here we'll reuse the 4th data point from the last example for
this purpose.

    >>> fdd = RecursiveFDD([p0, p1, p2], error_point=p3)
    >>> fdd.error(2)
    0.06292320000000011
