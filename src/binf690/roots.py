"""Estimate roots of functions.

"""


def bisect(f, xl, xu, es, itermax):
    yl = f(xl)
    xr = xl
    for i in range(itermax):
        xold = xr
        xr = (xl + xu) / 2
        yr = f(xr)
        if xr == 0:
            ea = 1.0
        else:
            ea = abs((xr - xold) / xr)

        # Test the sign and adjust the boundaries
        t = yl * yr
        if t < 0:
            xu = xr
        elif t > 0:
            xl = xr
            yl = yr
        else:
            ea = 0

        if ea < es:
            # Our error is small enough, so we stop early
            break

    return (xr, yr)
