"""Numerical methods to compute Eigenvalues.

Alexander Smith
BINF690
George Mason University
Fall 2020

"""


import numpy as np
from numpy.linalg import inv

from binf690.numeric import eps

ERROR_TOLERANCE = eps * 2**10


def power_method(m, h=1, debug=False):
    """Power method of computing eigen values and eigen vectors."""
    m = m.copy() / h
    x1 = np.ones(m.shape[0])
    v = 0
    dv = 1
    i = 0
    while dv > ERROR_TOLERANCE:
        if debug:
            print(f'i: {i} v: {v:.3f} dv: {dv:.3f}')
            print(x1)
        i += 1
        x2 = np.matmul(m, x1)
        v_next = np.max(np.abs(x2))
        dv = abs(v_next - v)
        v = v_next
        x1 = x2 / v
    return v, x1


def eigen_max(m, h=1):
    """Compute the highest eigen value and corresponding eigen vector."""
    return power_method(m, h=h)


def eigen_min(m, h=1):
    """Compute the lowest eigen value and corresponding eigen vector."""
    eig_val, eig_vec = power_method(inv(m.copy()), h=h)
    return (1.0 / eig_val, eig_vec)
