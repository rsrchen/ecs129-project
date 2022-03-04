from time import sleep
from modules import set_up_coord_files, shift_to_barycenters
from modules import eigenvalues_of_vector_F
from modules import calc_rmsd
from modules import generate_plots
from modules import set_up_coord_files
from tqdm import tqdm
from random import randint

"""
TODO:
- make it runnable w/ command line arguments. 4 letter code of protein, directory containing your pdb files, directory containing your coordinate files, etc. 
- make it accept 1 sequence. less hard-coded, more free. have it accept 1 sequence. or 4. or 12. not always 2 only. 
"""


def main(
    pdb_id: str, colabfold_hash: str, chains: str, predictions_dir: str, solved_dir: str
):
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

    # loading bar for fun. it's entirely unnecessary. haha.
    # print("Working...")
    # for i in tqdm(range(randint(90, 110))):
    #     sleep(0.005)

    # produce a dictionary of alpha carbon coordinates from AlphaFold's structure predictions.
    # contains at least 5 entries. probably more. i need to figure out how to separate them based on sequence
    # i'll do that later
    alpha_carbon_coords_dictionary = set_up_coord_files.main(
        pdb_id, colabfold_hash, chains, predictions_dir, solved_dir
    )
    if not alpha_carbon_coords_dictionary:
        print(
            "The length of the sequence corresponding to your solved structure is 0. Make sure you've selected the correct chain."
        )
        return 0

    # the alpha carbon coords dictionary looks like this:
    # {"rank1": [[x1,y1,z1],[x2,y2,z2], ...], "rank2": [[x1,y1,z1],[x2,y2,z2], ...], ...}
    #
    rmsd_catalog = {}
    for key_1, coordinates_array_1 in alpha_carbon_coords_dictionary.items():
        for key_2, coordinates_array_2 in alpha_carbon_coords_dictionary.items():
            shifted1, shifted2 = shift_to_barycenters.shift(
                coordinates_array_1, coordinates_array_2
            )
            max_eigenvalue = eigenvalues_of_vector_F.find(shifted1, shifted2)
            if not max_eigenvalue:
                return 0
            rmsd = round(calc_rmsd.calc(shifted1, shifted2, max_eigenvalue), 4)
            rmsd_catalog[key_1 + " and " + key_2] = rmsd

    # then it's time for sequence 2 comparisons.

    # print the results of our comparisons. the RMSDs.
    for name, rmsd in rmsd_catalog.items():
        print(name, "RMSD:", rmsd)

    generate_plots.generate(rmsd_catalog, pdb_id, chains)
    return 1
