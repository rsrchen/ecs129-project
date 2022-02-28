import numpy as np


def shift(
    first_x: list[float],
    first_y: list[float],
    first_z: list[float],
    second_x: list[float],
    second_y: list[float],
    second_z: list[float],
):

    # alpha carbon coordinates
    first_all_atoms_coords = list(zip(first_x, first_y, first_z))
    # calculating component average
    avg_first_x = np.mean(first_x)
    avg_first_y = np.mean(first_y)
    avg_first_z = np.mean(first_z)

    first_barycenter = [avg_first_x, avg_first_y, avg_first_z]

    # alpha carbon coordinates
    second_all_atoms_coords = list(zip(second_x, second_y, second_z))
    # calculating component average
    avg_second_x = np.mean(second_x)
    avg_second_y = np.mean(second_y)
    avg_second_z = np.mean(second_z)

    second_barycenter = [avg_second_x, avg_second_y, avg_second_z]

    xtild = np.subtract(first_all_atoms_coords, first_barycenter)
    # Calculating y-tilde
    ytild = np.subtract(second_all_atoms_coords, second_barycenter)
    return (xtild, ytild)
