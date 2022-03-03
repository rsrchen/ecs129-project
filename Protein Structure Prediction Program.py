import sys

print("Number of arguments:", len(sys.argv), "arguments.")
print("Argument List:", str(sys.argv))

"""
so. how's it gonna be?

default settings:
ingest one sequence only
ask for 4 character PDB ID code, else crash
directory containing PDB file is ./pdb_files
directory containing coordinate files (seq1rank1 thru seq1goldstandard) is ./coordinate_files

changeable settings:
# of sequences to do rmsd shit for
PDB files directory
coords txt files directory

steps:
1. generate pdb file of only alpha carbons, nicely formatted, spaces where they ought to be
2. generate alpha carbon coords plaintext file from that ^ and put it in coordinate files (goodbye awk. it'll be too hard for me to reach into the WSL via python. i'll have to code this myself.)
3. read that coordinate file and do the rmsd shit!
4. repeat for all the sequences the user inputs

"""