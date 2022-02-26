    #creating tuples containing alpha carbon coordinates
    xi = zip(x,y,z)
    #calculate Gx
    n = len(xlist)

    def Average(lst):
        return sum(lst) / n
    
    Gx = Average(lst)
    #calculate xtilda
    xtild = []
    cord = zip(x,y,z)
