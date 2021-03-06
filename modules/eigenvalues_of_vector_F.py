# plug each value of the matrix R into the F matrix
# find the max eigenvalue from the F matrix

import numpy as np
from numpy import linalg as lg


def find(
    x_tilde: list[list[float, float, float]], y_tilde: list[list[float, float, float]]
):
    # create the R matrix based on x-tilde and y-tilde
    matrix_r = np.zeros((3, 3))  # empty 3x3 matrix
    for i in range(0, 3):
        for j in range(0, 3):
            sum_for_r_i_j = 0
            for n in range(len(x_tilde)):
                try:
                    sum_for_r_i_j += x_tilde[n][i] * y_tilde[n][j]
                except IndexError:
                    print(
                        "Error: Python reported an IndexError when the program attempted to generate matrix R. Make sure your predicted structures and solved structure are of the same length, and make sure you've entered chain(s) that are valid and correct."
                    )
                    return 0
            matrix_r[i, j] = sum_for_r_i_j

    # plug the corresponding values into the matrix F
    matrix_f = np.zeros((4, 4))  # create empty 4x4 matrix
    # create matrix F with the values from the rmsd paper
    matrix_f[0, 0] = matrix_r[0, 0] + matrix_r[1, 1] + matrix_r[2, 2]
    matrix_f[0, 1] = matrix_r[1, 2] - matrix_r[2, 1]
    matrix_f[0, 2] = matrix_r[2, 0] - matrix_r[0, 2]
    matrix_f[0, 3] = matrix_r[0, 1] - matrix_r[1, 0]

    matrix_f[1, 0] = matrix_r[1, 2] - matrix_r[2, 1]
    matrix_f[1, 1] = matrix_r[0, 0] - matrix_r[1, 1] - matrix_r[2, 2]
    matrix_f[1, 2] = matrix_r[0, 1] + matrix_r[1, 0]
    matrix_f[1, 3] = matrix_r[0, 2] + matrix_r[2, 0]

    matrix_f[2, 0] = matrix_r[2, 0] - matrix_r[0, 2]
    matrix_f[2, 1] = matrix_r[0, 1] + matrix_r[1, 0]
    matrix_f[2, 2] = -matrix_r[0, 0] + matrix_r[1, 1] - matrix_r[2, 2]
    matrix_f[2, 3] = matrix_r[1, 2] + matrix_r[2, 1]

    matrix_f[3, 0] = matrix_r[0, 1] - matrix_r[1, 0]
    matrix_f[3, 1] = matrix_r[0, 2] + matrix_r[2, 0]
    matrix_f[3, 2] = matrix_r[1, 2] + matrix_r[2, 1]
    matrix_f[3, 3] = -matrix_r[0, 0] - matrix_r[1, 1] + matrix_r[2, 2]

    # use linalg to find the eigenvalues and eigenvectors
    vals, vects = lg.eig(matrix_f)
    maxvalue = max(vals)  # determining max eigenvalue
    return maxvalue
