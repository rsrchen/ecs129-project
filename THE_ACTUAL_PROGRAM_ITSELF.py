import modules.shift_to_barycenters as shift_to_barycenters, modules.eigenvalues_of_vector_F as eigenvalues_of_vector_F, modules.calc_rmsd as calc_rmsd


def main():
    """
    Determine the root-mean-square deviation between AlphaFold's protein structure predictions and the true protein structure as determined by crystallography/other empirical experimental methods by comparing the 3-D paths of their alpha carbon backbones through space. For our purposes, this program will only perform comparisons between a predetermined set of structures:
        5 AlphaFold predictions of CTC1 structure and 1 experimentally determined CTC1 structure
        5 AlphaFold predictions of fimbrial adhesin structure and 1 experimentally determined fimbrial adhesin structure
    All AlphaFold predictions of CTC1 structure will be compared to each other, as well as to the experimentally determined CTC1 structure, resulting in 36 comparisons between CTC1 structures. Same goes for all of the fimbrial adhesin structures; they'll all be compared to one another.

    These are the steps the program will take:
    1. Process a set of .txt files containing the x, y, and z coordinates of all of the alpha carbons of a protein structure. The x, y, and z coordinates of a single alpha carbon atom should all be written on one line. The coordinates themselves should be separated from each other by a single space. The coordinates for the next alpha carbon atom go on the next line, and so on and so forth.
    2. Lay the structures atop one another by shifting them all to their barycenters (average coordinate/center of mass/center of gravity).
    3. Calculate the maximum eigenvalue and corresponding eigenvector of matrix F, calculated from the structures' alpha carbon coordinates after having been shifted to their barycenters, to account for structure rotation.
    4. Calculate the root-mean-square deviation between the two structures.

    """
    print("ECS 129 Protein Structure Comparison Program")

    all_seq1_structures: dict[str, dict[str, list[float]]] = {}
    all_seq2_structures: dict[str, dict[str, list[float]]] = {}
    # the plan is to loop through the lines and stop at each whitespace encounter, take the first thing, put it into an x list, take the second thing, y list, third thing z list. each entry in the dictionary all_seq1_structures will contain a dictionary itself. that internal dictionary will contain x: [list of x's], y: [list of y's] you get the point

    # read seq1 coord files.
    location_of_coordinate_files = "coordinate files"
    for i in range(1, 6):
        key_name = "seq1rank" + str(i)
        filename = key_name + ".txt"
        with open(
            location_of_coordinate_files + "/" + filename
        ) as alpha_carbon_coordinate_file:
            xlist = []
            ylist = []
            zlist = []
            for line in alpha_carbon_coordinate_file:
                split_line = line.split()
                xlist.append(float(split_line[0]))
                ylist.append(float(split_line[1]))
                zlist.append(float(split_line[2]))
            all_seq1_structures[key_name] = {
                "x": xlist,
                "y": ylist,
                "z": zlist,
            }
    # read seq2 coord files.
    for i in range(1, 6):
        key_name = "seq2rank" + str(i)
        filename = key_name + ".txt"
        with open(
            location_of_coordinate_files + "/" + filename
        ) as alpha_carbon_coordinate_file:
            xlist = []
            ylist = []
            zlist = []
            for line in alpha_carbon_coordinate_file:
                split_line = line.split()
                xlist.append(float(split_line[0]))
                ylist.append(float(split_line[1]))
                zlist.append(float(split_line[2]))
            all_seq2_structures[key_name] = {
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
        all_seq1_structures["seq1goldstandard"] = {
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
        all_seq2_structures["seq2goldstandard"] = {
            "x": xlist,
            "y": ylist,
            "z": zlist,
        }

    pass

    # the plan: entry_1 and entry_2 are both dictionaries that look like
    # { "x": [1,2,3], "y": [1,2,3], "z": [1,2,3] }
    # need to shift entry_1 and entry_2 to their barycenters
    # then need to calculate the eigen shit of entry_1 and entry_2
    # i could be more efficient if i didn't repeat calculations. but fuck that
    #

    for entry_1 in all_seq1_structures.values():
        for entry_2 in all_seq1_structures.values():
            shifted1, shifted2 = shift_to_barycenters.shift(
                entry_1["x"],
                entry_1["y"],
                entry_1["z"],
                entry_2["x"],
                entry_2["y"],
                entry_2["z"],
            )
            max_eigenvalue = eigenvalues_of_vector_F.find(shifted1, shifted2)
            calc_rmsd.calc()

    # for entry_1 in all_seq2_structures.values():
    #     for entry_2 in all_seq2_structures.values():
    #         shift_to_barycenters.shift(entry_1)
    #         eigenvalues_of_vector_F.find()
    #         calc_rmsd.calc()


main()
