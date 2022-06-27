from modules import parse_pdb
from pathlib import Path

pdb_file_name = input("Enter name of PDB file, e.g. 1A2Y.pdb\n")
solved = input("Is this a solved structure? Enter yes or no, e.g. yes\n")
chains = input("Enter chains, e.g. AB\n")
if solved == "yes":
    use_chains = True
else: 
    use_chains = False

p = Path("./")
# assuming there's only one file that contains this name
path_to_pdb_file = list(p.glob("**/" + pdb_file_name))

print("Length of sequence specified:", len(parse_pdb.get_alpha_carbons(path_to_pdb_file[0], "____", chains.upper(), use_chains=use_chains)))