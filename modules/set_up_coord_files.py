from pathlib import Path
import numpy as np

# import awk_but_not_really
from modules import parse_pdb

def main(
    pdb_id: str,
    colabfold_hash: str,
    chains_prediction: str,
    chains_solved: str,
    path_to_alphafold_predictions: str | Path,
    path_to_solved_structures: str | Path,
):
    p = Path("./")
    alpha_carbons_dictionary = {}
    alphafold_prediction_pdb_files = p.glob(
        f"{path_to_alphafold_predictions}/*{colabfold_hash}*.pdb"
    )
    # there will always be 5 alphafold prediction files for one sequence ordered from rank 1 to rank 5 in this directory.
    # there may be more than 5 files in here in total, but they will come from different sequences.
    # the total will always be a multiple of 5.
    rank = 1
    for file in alphafold_prediction_pdb_files:
        alpha_carbons_dictionary[
            pdb_id + "_rank" + str(rank)
        ] = parse_pdb.get_alpha_carbons(file, pdb_id, chains_prediction)
        rank += 1

    # there should only be one.
    solved_structure_pdb_file = list(
        (p.glob(f"{path_to_solved_structures}/*{pdb_id}*.pdb"))
    )
    alpha_carbons_dictionary[pdb_id + "_goldstandard"] = parse_pdb.get_alpha_carbons(
        solved_structure_pdb_file[0], pdb_id, chains_solved
    )
    # this will probably only happen if the chain is incorrect.
    if len(alpha_carbons_dictionary[pdb_id + "_goldstandard"]) == 0:
        return 0
    # this will only happen if the structure has missing residues.
    if len(alpha_carbons_dictionary[pdb_id + "_goldstandard"]) and np.all(
        alpha_carbons_dictionary[pdb_id + "_goldstandard"][0] == -1
    ):
        return -1
    return alpha_carbons_dictionary
