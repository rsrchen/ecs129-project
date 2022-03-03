import sys
import regex
from pathlib import Path
import main_program

"""
so. how's it gonna be?

default settings:
directory containing alphafold prediction PDB files is ./alphafold_predictions
directory containing true structure PDB files is ./solved_structures
chain A
require colabfold hash, exit if it's not given. needs to be valid; it'll be checked.
require 4 character PDB ID, exit if it's not given. needs to be valid. it'll be checked.

changeable settings:
PDB ID
which chains to look at from the experimentally-determined structure
colabfold hash
PDB files directory
true structures directory

overview:
1. read pdb files of alphafold's structure predictions 
2. get alpha carbon coordinates
3. read pdb file of the true structure
4. get alpha carbon coordinates
5. compute rmsd
6. $$$$$$$$$$$$$$$$$$$$$$$$

"""


def main():
    colabfold_jobname_hash = None
    pdb_id = None
    chains = "A"
    predictions_dir = "alphafold_predictions"
    solved_dir = "solved_structures"
    strung_out = " "
    for x in sys.argv:
        strung_out += x + " "
    flags_entered = regex.findall(r"\s-\S\s", strung_out)
    valid_flags = [" -a ", " -s ", " -p ", " -h ", " -c "]

    for flag in flags_entered:
        if flag not in valid_flags:
            print("Invalid flags detected.")
            return 0

    valid_flags = [flag.strip() for flag in valid_flags]

    # -a is the flag people will use to indicate alphafold predictions PDB files directory
    if "-a" in sys.argv:
        try:
            predictions_dir = sys.argv[sys.argv.index("-a") + 1]
            if predictions_dir in valid_flags:
                print("Error: invalid argument provided for -a.")
                return 0
        except IndexError:
            print(
                "No argument provided for -a; default predicted structures directory (./alphafold_predictions) will be used."
            )
    else:
        print(
            "No argument provided for -a; default predicted structures directory (./alphafold_predictions) will be used."
        )

    # -s is for solved structures directory
    if "-s" in sys.argv:
        try:
            solved_dir = sys.argv[sys.argv.index("-s") + 1]
            if solved_dir in valid_flags:
                print("Error: invalid argument provided for -s.")
                return 0
        except IndexError:
            print(
                "No argument provided for -s; default solved structures directory (./solved_structures) will be used."
            )
    else:
        print(
            "No argument provided for -s; default solved structures directory (./solved_structures) will be used."
        )

    # -p is the pdb id
    if "-p" in sys.argv:
        try:
            pdb_id = sys.argv[sys.argv.index("-p") + 1]
            if pdb_id in valid_flags:
                print("Error: invalid argument provided for -p.")
                return 0
        except IndexError:
            print("Error: no argument provided for -p.")
            return 0

    # -h is the colabfold structure name hash. the 5 character code in the name that comes before "unrelaxed"
    if "-h" in sys.argv:
        try:
            colabfold_jobname_hash = sys.argv[sys.argv.index("-h") + 1]
            if colabfold_jobname_hash in valid_flags:
                print("Error: invalid argument provided for -h.")
                return 0
        except IndexError:
            print("Error: no argument provided for -h.")
            return 0

    # -c is which chain. or chains. A chain, B chain, C, D, etc. entered like "A" or "ABC", alphabetically
    if "-c" in sys.argv:
        try:
            chains = sys.argv[sys.argv.index("-c") + 1]
            if chains in valid_flags:
                print("Error: invalid argument provided for -c.")
                return 0
        except IndexError:
            print("No argument provided for -c; default chain A will be used.")
    else:
        print("No argument provided for -c; default chain A will be used.")

    if not pdb_id:
        print("Error: PDB ID cannot be empty.")
        return 0
    if not colabfold_jobname_hash:
        print("Error: ColabFold structure name hash cannot be empty.")
        return 0
    some_path = Path(predictions_dir)
    if not some_path.exists():
        print(f'Error: directory "{predictions_dir}" does not exist.')
        return 0
    some_path = Path(solved_dir)
    if not some_path.exists():
        print(f'Error: directory "{solved_dir}" does not exist.')
        return 0
    some_path = Path(f"{solved_dir}/{pdb_id}.pdb")
    if not some_path.exists():
        print(f"Error: {pdb_id}.pdb does not exist.")
        return 0
    some_path = Path(f"{predictions_dir}")
    all_predictions_with_a_given_hash = list(
        some_path.glob(f"*{colabfold_jobname_hash}*.pdb")
    )
    if not all_predictions_with_a_given_hash:
        print(f"Error: invalid ColabFold structure name hash given. ")
        return 0
    if len(all_predictions_with_a_given_hash) != 5:
        print(
            f"Error: there must be exactly 5 AlphaFold structure predictions per protein in the AlphaFold prediction directory."
        )
        return 0
    return (pdb_id, colabfold_jobname_hash, chains, predictions_dir, solved_dir)


go = main()

# if main goes off without a hitch
if go:
    main_program.main(go[0], go[1], go[2], go[3], go[4])
    pass
else:
    print("Program execution aborted.")
