# #creating tuples containing alpha carbon coordinates
# xi = zip(x,y,z)
# #calculate Gx
# n = len(xlist)

# def Average(lst):
#     return sum(lst) / n

# Gx = Average(lst)
# #calculate xtilda
# xtild = []
# cord = zip(x,y,z)

import numpy as np


def shift(
    first_x: list[float],
    first_y: list[float],
    first_z: list[float],
    second_x: list[float],
    second_y: list[float],
    second_z: list[float],
):
    def average(lst):
        return sum(lst) / len(lst)

    # alpha carbon coordinates
    first_all_atoms_coords = list(zip(first_x, first_y, first_z))
    # calculating component average
    avg_first_x = average(first_x)
    avg_first_y = average(first_y)
    avg_first_z = average(first_z)

    first_barycenter = [avg_first_x, avg_first_y, avg_first_z]

    # alpha carbon coordinates
    second_all_atoms_coords = list(zip(second_x, second_y, second_z))
    # calculating component average
    avg_second_x = average(second_x)
    avg_second_y = average(second_y)
    avg_second_z = average(second_z)

    second_barycenter = [avg_second_x, avg_second_y, avg_second_z]

    xtild = np.subtract(first_all_atoms_coords, first_barycenter)
    # Calculating y-tilde
    ytild = np.subtract(second_all_atoms_coords, second_barycenter)
    return (xtild, ytild)
