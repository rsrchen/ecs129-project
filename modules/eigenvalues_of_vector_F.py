# # xtilda(n) = vector(n) - G(X)
# # ytilda(n) = vector(n) - G(x)
# # plug in [1,3] into the summation
# # create the new matrix R
# def matrixR(i,j):


# # plug each value of the matrix R into the F matrix
# # find the max eigenvalue from the F matrix

import numpy as np
from numpy import linalg as lg

def find(x_tilde: list[list[float, float, float]], y_tilde: list[list[float, float, float]]):
    # create the R matrix based on x-tilde and y-tilde
    matrix_r = np.zeros((3, 3))  # empty 3x3 matrix
    for i in range(0, 3):
        for j in range(0, 3):
          sum_for_r_i_j = 0
          for n in range(len(x_tilde)): 
            sum_for_r_i_j += (x_tilde[n][i] * y_tilde[n][j])
          matrix_r[i, j] = sum_for_r_i_j
    print("Matrix R:\n", matrix_r)

    # not sure about this stuff up here. may need to be fixed. 
    # screw it. i'll fix it myself. 


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
    print("Matrix F:\n", matrix_f)

    # use linalg to find the eigenvalues and eigenvectors
    vals, vects = lg.eig(matrix_f)
    print("eigenvalues:\n", vals)  # eigenvalues
    print("eigenvectors:\n", vects)  # eigenvectors
    maxvalue = max(vals)  # determining max eigenvalue
    print("max eigenvalue:\n", maxvalue)  # max eigenvalue
    return maxvalue
