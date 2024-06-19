from typing import Literal
from modules import parse_pdb
from pathlib import Path
import sys
import regex

"""
a new way of doing things: cli
it's just better and faster for the user

flags:
-n name of pdb file
-c chains (use same logic as command_line.py)
"""

def cli():
    print("\nPDB File Length Finder\n")
    name = None
    chains = "A"
    strung_out = " "
    for x in sys.argv:
        strung_out += x + " "
    flags_entered = regex.findall(r"\s-\S\s", strung_out)
    valid_flags = [" -n ", " -c "]

    for flag in flags_entered:
        if flag not in valid_flags:
            print("Invalid flags detected.")
            return 0

    valid_flags = [flag.strip() for flag in valid_flags]

    if "-n" in sys.argv:
        name = sys.argv[sys.argv.index("-n") + 1]

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

    if not name:
        print("Error: no filename provided.")
        return 0

    return (name, chains)

info: Literal[0] | tuple[str, bool, str] = cli()
if info == 0:
    raise ValueError("Program execution aborted.")

pdb_file_name = info[0]
chains = info[1]

p = Path("./")
# assuming there's only one file that contains this name
path_to_pdb_file = list(p.glob("**/" + pdb_file_name))

print(
    "Length of sequence specified:",
    len(
        parse_pdb.get_alpha_carbons(
            path_to_pdb_file[0], "____", chains.upper()
        )
    ),
)



