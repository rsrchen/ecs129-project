from modules import set_up_coord_files, shift_to_barycenters
from modules import eigenvalues_of_vector_F
from modules import calc_rmsd
from modules import generate_plots
from modules import set_up_coord_files

"""
TODO:
- make it runnable w/ command line arguments. 4 letter code of protein, directory containing your pdb files, directory containing your coordinate files, etc. 
- make it asynchronous. have it do shit to a file, wait for the file to get written to, pick up right there, etc. the parsing and awking and stuff. 
- make it accept 1 sequence. less hard-coded, more free. have it accept 1 sequence. or 4. or 12. not always 2 only. 
"""


def main(pdb_id: str, predictions_dir: str, solved_dir: str):
    """
    Determine the root-mean-square deviation between AlphaFold's protein structure predictions and
    the true protein structure as determined by crystallography/other empirical experimental
    methods by comparing the 3-D paths of their alpha carbon backbones through space. For our
    purposes, this program will only perform comparisons between a predetermined set of
    structures:
        5 AlphaFold predictions of CTC1 structure and 1 experimentally determined CTC1 structure
        5 AlphaFold predictions of fimbrial adhesin structure and 1 experimentally determined
        fimbrial adhesin structure
    All AlphaFold predictions of CTC1 structure will be compared to each other, as well as to
    the experimentally determined CTC1 structure, resulting in 36 comparisons between CTC1
    structures. Same goes for all of the fimbrial adhesin structures; they'll all be compared
    to one another.

    These are the steps the program will take:
    1. Process a set of .txt files containing the x, y, and z coordinates of all of the alpha
    carbons of a protein structure. The x, y, and z coordinates of a single alpha carbon atom
    should all be written on one line. The coordinates themselves should be separated from each
    other by a single space. The coordinates for the next alpha carbon atom go on the next line,
    and so on and so forth.
    2. Lay the structures atop one another by shifting them all to their barycenters (average
    coordinate/center of mass/center of gravity).
    3. Calculate the maximum eigenvalue and corresponding eigenvector of matrix F, calculated
    from the structures' alpha carbon coordinates after having been shifted to their
    barycenters, to account for structure rotation.
    4. Calculate the root-mean-square deviation between the two structures.
    5. Print all root-mean-square deviations between all structures of a protein, rounded to
    4 decimal places. Root-mean-square deviations that are very low will be rounded to zero.

    """
    print()
    print("================================================")
    print("ECS 129 Protein Structure Comparison Program")
    print(
        "This program calculates and outputs root-mean-square deviations between two protein structures. Check the main() docstring for more details."
    )
    print("================================================")
    print()

    # produce a dictionary of alpha carbon coordinates from AlphaFold's structure predictions.
    alpha_carbon_coords_dictionary = set_up_coord_files.execute("pdb_files", "1ab1")

    # coordinates_dict_1 and 2 are both dictionaries that look like
    # { "x": [1,2,3], "y": [1,2,3], "z": [1,2,3] }
    # now it's time to get to work comparing everything to everything.
    # sequence 1 comparisons first.
    seq1_rmsd_catalog = {}
    for key_1, coordinates_dict_1 in all_seq1_structures.items():
        for key_2, coordinates_dict_2 in all_seq1_structures.items():
            shifted1, shifted2 = shift_to_barycenters.shift(
                coordinates_dict_1["x"],
                coordinates_dict_1["y"],
                coordinates_dict_1["z"],
                coordinates_dict_2["x"],
                coordinates_dict_2["y"],
                coordinates_dict_2["z"],
            )
            max_eigenvalue = eigenvalues_of_vector_F.find(shifted1, shifted2)
            rmsd = round(calc_rmsd.calc(shifted1, shifted2, max_eigenvalue), 4)
            seq1_rmsd_catalog[key_1 + " and " + key_2] = rmsd

    # then it's time for sequence 2 comparisons.
    seq2_rmsd_catalog = {}
    for key_1, coordinates_dict_1 in all_seq2_structures.items():
        for key_2, coordinates_dict_2 in all_seq2_structures.items():
            shifted1, shifted2 = shift_to_barycenters.shift(
                coordinates_dict_1["x"],
                coordinates_dict_1["y"],
                coordinates_dict_1["z"],
                coordinates_dict_2["x"],
                coordinates_dict_2["y"],
                coordinates_dict_2["z"],
            )
            max_eigenvalue = eigenvalues_of_vector_F.find(shifted1, shifted2)
            rmsd = round(calc_rmsd.calc(shifted1, shifted2, max_eigenvalue), 4)
            seq2_rmsd_catalog[key_1 + " and " + key_2] = rmsd

    # print the results of our comparisons. the RMSDs.
    for name, rmsd in seq1_rmsd_catalog.items():
        print(name, "RMSD:", rmsd)

    for name, rmsd in seq2_rmsd_catalog.items():
        print(name, "RMSD:", rmsd)

    generate_plots.generate(seq1_rmsd_catalog)
    generate_plots.generate(seq2_rmsd_catalog)


