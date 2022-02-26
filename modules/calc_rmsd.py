import math

def calc(x_tilde_k, y_tilde_k, max_eigenvalue):
    # calculating rmsd
    # for values of the coordinate points add up the x-tilde
    for i in range(len(x_tilde_k)):
        xk += sum(x_tilde_k[i])
    # for values of the coordinate points add up the y-tilde
    for i in range(len(y_tilde_k)):
        yk += sum(y_tilde_k[i])
    # compute xtilda and ytilda squared

    xtild_squared = xk**2
    ytild_squared = yk**2
    print(xtild_squared)
    print(ytild_squared)
    # find the sum of the xtilda and ytilda squared
    n = int(len(xi))
    for i in range(1, n):
        for j in range(1, n):
            sum1 = xtild_squared + ytild_squared
    print("sum:", sum1)
    # compute 2 * lambda max
    two_max = 2 * maxvalue  # 2* lambda max
    # compute rmsd
    rmsd = math.sqrt((sum1 - two_max) / int(len(xi)))
    print("rmsd:", rmsd)
