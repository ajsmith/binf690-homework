================
Gradient Methods
================


    >>> from binf690.gradient import Hessian
    >>> from binf690.hw5 import f, dfdx, dfdy, d2fdx2, d2fdy2, d2fdxdy

Testing the Hessian

    >>> x, y = (0.0, 0.0)
    >>> H = Hessian(d2fdx2, d2fdy2, d2fdxdy)
    >>> H(x, y)
    12

Centered finite divided difference

    >>> from binf690.gradient import centered_fdd_func
    >>> fdd = centered_fdd_func(lambda x: x**3)
    >>> fdd(100)
    30000.0

Creating g(h)

    >>> from binf690.gradient import x_coord_func, y_coord_func, g_func
    >>> dfdx(x, y)
    -8.0
    >>> dfdy(x, y)
    12.0
    >>> xh = x_coord_func(x, y, dfdx)
    >>> xh(1)
    -8.0
    >>> yh = y_coord_func(x, y, dfdy)
    >>> yh(1)
    12.0
    >>> g = g_func(f, xh, yh)
    >>> g(1)
    1040.0
    >>> g(1) == f(xh(1), yh(1))
    True

    >>> dgdh = centered_fdd_func(g)
    >>> dgdh(1)
    1872.0

    >>> x, y = (1, 2)
    >>> dfdx(x, y)
    -10
    >>> dfdy(x, y)
    26
    >>> xh = x_coord_func(x, y, dfdx)
    >>> xh(1)
    -9
    >>> yh = y_coord_func(x, y, dfdy)
    >>> yh(1)
    28
    >>> g = g_func(f, xh, yh)
    >>> g(1)
    4129
    >>> g(1) == f(xh(1), yh(1))
    True
