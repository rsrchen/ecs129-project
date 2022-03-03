from pathlib import Path

# import awk_but_not_really
from modules import parse_pdb


def execute(path_to_pdb_files_directory: str | Path, pdb_id: str):
    p = Path("./")
    alpha_carbons_dictionary = {}
    alphafold_prediction_pdb_files = p.glob(path_to_pdb_files_directory + "/*.pdb")
    # there will always be 5 alphafold prediction files for one sequence ordered from rank 1 to rank 5 in this directory.
    # there may be more than 5 files in here in total, but they will come from different sequences.
    # the total will always be a multiple of 5.
    rank = 1
    for file in alphafold_prediction_pdb_files:
        alpha_carbons_dictionary[
            pdb_id + "_rank" + str(rank)
        ] = parse_pdb.get_alpha_carbons(file, "1ab1")
        rank += 1
    return alpha_carbons_dictionary
