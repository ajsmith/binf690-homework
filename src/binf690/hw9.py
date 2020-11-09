"""Homework 9

Alexander Smith
BINF690
George Mason University
Fall 2020

"""

import numpy as np

from binf690.eigen import eigen_min, eigen_max


def hw9():
    A = np.array(
        [
            [2, 8, 10],
            [8, 4, 5],
            [10, 5, 7],
        ],
        dtype='float64',
    )

    print('Matrix Input:')
    print(A)

    eig_max, eig_vec = eigen_max(A)
    print(f'Highest Eigen Value: {eig_max:.3f}')
    print('Eigen Vector:', eig_vec)

    eig_min, eig_vec = eigen_min(A)
    print(f'Lowest Eigen Value: {eig_min:.3f}')
    print('Eigen Vector:', eig_vec, 3)
