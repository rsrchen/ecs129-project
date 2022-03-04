import numpy as np


def shift(first_coords_list: list[list[float]], second_coords_list: list[list[float]]):

    
    # calculating averages of the first set of alpha carbons
    avg_first_x = np.mean(list(zip(*first_coords_list))[0])
    avg_first_y = np.mean(list(zip(*first_coords_list))[1])
    avg_first_z = np.mean(list(zip(*first_coords_list))[2])

    first_barycenter = [avg_first_x, avg_first_y, avg_first_z]

    # now the second
    avg_second_x = np.mean(list(zip(*second_coords_list))[0])
    avg_second_y = np.mean(list(zip(*second_coords_list))[1])
    avg_second_z = np.mean(list(zip(*second_coords_list))[2])

    second_barycenter = [avg_second_x, avg_second_y, avg_second_z]

    xtild = np.subtract(first_coords_list, first_barycenter)
    # Calculating y-tilde
    ytild = np.subtract(second_coords_list, second_barycenter)
    return (xtild, ytild)
