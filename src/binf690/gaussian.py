"""Gaussian Elimination for solving systems of linear equations.


Alexander Smith
BINF690
George Mason University
Fall 2020
"""

import numpy as np
from binf690.numeric import eps


TOLERANCE = eps * 10**6


def gauss_elimination(a, b, n, tol=TOLERANCE):
    s = []
    for i in range(n):
        s.append(max(abs(e) for e in a[i]))
    s = np.array(s)
    eliminate(a, b, n, s, tol)

    det = 1
    for i in range(n):
        det *= a[i, i]
    if abs(det) < tol:
        raise ValueError(f'Determinant near zero: {det}')

    x = substitute(a, b, n)
    return x.flatten()


def eliminate(a, b, n, s, tol):
    for k in range(n - 1):
        pivot(a, b, n, s, k)
        if abs(a[k, k]) < tol:
            raise ValueError(f'a[{k}, {k}] < {tol}')

        for i in range(k + 1, n):
            factor = a[i, k] / a[k, k]
            a[i] = a[i] - factor * a[k]
            b[i] = b[i] - factor * b[k]

    i = n - 1
    if abs(a[i, i] / s[i]) < tol:
        raise ValueError(f'abs(a[{i}, {i}] / s[i]) < {tol}')


def pivot(a, b, n, s, k):
    p = k
    big = abs(a[k, k] / s[k])
    for i in range(k + 1, n):
        dummy = abs(a[i, k] / s[i])
        if dummy > big:
            big = dummy
            p = i

    if p != k:
        a[[k, p]] = a[[p, k]]
        b[[k, p]] = b[[p, k]]
        s[[k, p]] = s[[p, k]]


def substitute(a, b, n):
    x = np.zeros(b.shape)
    x[-1] = b[-1] / a[-1, -1]
    for i in range(1, n):
        i = n - i - 1
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] = x[i] - a[i, j] * x[j]
        x[i] = x[i] / a[i, i]
    return x
