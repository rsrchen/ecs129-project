# import modules.shift_to_barycenters as shift_to_barycenters, modules.eigenvalues_of_vector_F as eigenvalues_of_vector_F, modules.calc_rmsd as calc_rmsd


def main():
    print("ECS 129 Protein Structure Comparison Program")
    # read the file(s) here. then send them to the individual modules
    # 5 alpha carbon coord files for alphafold's prediction of ctc1 structure, 5 alpha carbon coord files for alphafold's prediction of fimbrial adhesin structure, 1 alpha carbon coord file for the gold standard of ctc1 structure, 1 alpha carbon coord file for the gold standard of fimbrial adhesin structure. in total, 12 alpha carbon coordinate files
    all_files = {}
    # the plan is to loop through the lines and stop at each whitespace encounter, take the first thing, put it into an x list, take the second thing, y list, third thing z list. each entry in the dictionary all_files will contain a dictionary itself. that internal dictionary will contain x: [list of x's], y: [list of y's] you get the point 
    
    # read seq1 coord files.
    location_of_coordinate_files = "coordinate files"
    for i in range(1, 6):
        filename = "seq1rank" + str(i) + ".txt"
        with open(location_of_coordinate_files + "/" + filename) as alpha_carbon_coordinate_file:
            xlist = []
            ylist = []
            zlist = []
            for line in alpha_carbon_coordinate_file:
                split_line = line.split()
                xlist.append(float(split_line[0]))
                ylist.append(float(split_line[1]))
                zlist.append(float(split_line[2]))
            all_files[filename] = {
                "x": xlist, 
                "y": ylist, 
                "z": zlist, 
            }
    # read seq2 coord files. 
    for i in range(1, 6):
        filename = "seq2rank" + str(i) + ".txt"
        with open(location_of_coordinate_files + "/" + filename) as alpha_carbon_coordinate_file:
            xlist = []
            ylist = []
            zlist = []
            for line in alpha_carbon_coordinate_file:
                split_line = line.split()
                xlist.append(float(split_line[0]))
                ylist.append(float(split_line[1]))
                zlist.append(float(split_line[2]))
            all_files[filename] = {
                "x": xlist, 
                "y": ylist, 
                "z": zlist, 
            }
    # read seq1 gold standard coord file.
    with open("coordinate files/seq1goldstandard.txt") as alpha_carbon_coordinate_file:
        xlist = []
        ylist = []
        zlist = []
        for line in alpha_carbon_coordinate_file:
            split_line = line.split()
            xlist.append(float(split_line[0]))
            ylist.append(float(split_line[1]))
            zlist.append(float(split_line[2]))
        all_files["seq1goldstandard.txt"] = {
            "x": xlist, 
            "y": ylist, 
            "z": zlist, 
        }
    
    # read seq2 gold standard coord file.
    with open("coordinate files/seq2goldstandard.txt") as alpha_carbon_coordinate_file:
        xlist = []
        ylist = []
        zlist = []
        for line in alpha_carbon_coordinate_file:
            split_line = line.split()
            xlist.append(float(split_line[0]))
            ylist.append(float(split_line[1]))
            zlist.append(float(split_line[2]))
        all_files["seq2goldstandard.txt"] = {
            "x": xlist, 
            "y": ylist, 
            "z": zlist, 
        }
    
    pass
    # ta-da! we've read all the files.
    
    # shift_to_barycenters()
    # eigenvalues_of_vector_F()
    # calc_rmsd()


main()
