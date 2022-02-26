import math

def calc():
    # calculating rmsd
    # for values of the coordinate points add up the x-tilde
    for i in range(1, len(xi)):
        xk = sum(xtild[i])
    # for values of the coordinate points add up the y-tilde
    for i in range(1, len(yi)):
        yk = sum(ytild[i])
    # compute xtilda and ytilda squared
    xtild_squared = xk**2
    ytild_squared = yk**2
    print(xtild_squared)
    print(ytild_squared)
    # find the sum of the xtilda and ytilda squared
    n = int(len(xi))
    for i in range(1, n):
        for j in range(1, n):
            sum = xtild_squared + ytild_squared
    print("sum:", sum)
    # compute 2 * lambda max
    two_max = 2 * maxvalue  # 2* lambda max
    # compute rmsd
    rmsd = math.sqrt((sum - two_max) / int(len(xi)))
    print("rmsd:", rmsd)
