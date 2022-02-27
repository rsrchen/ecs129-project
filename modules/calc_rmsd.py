from math import sqrt


def calc(x_tilde_k, y_tilde_k, max_eigenvalue):
    # calculating rmsd
    total_summation = 0
    for n in range(len(x_tilde_k)):
        x_k_squared = x_tilde_k[n][0] ** 2 + x_tilde_k[n][1] ** 2 + x_tilde_k[n][2] ** 2
        y_k_squared = y_tilde_k[n][0] ** 2 + y_tilde_k[n][1] ** 2 + y_tilde_k[n][2] ** 2
        sum_of_them_two = x_k_squared + y_k_squared
        total_summation += sum_of_them_two
    try:
        rmsd = sqrt(abs(total_summation - 2 * max_eigenvalue) / len(x_tilde_k))
        return rmsd
    except ValueError:
        rmsd = "ValueError encountered while trying to calculate RMSD."
        return rmsd
