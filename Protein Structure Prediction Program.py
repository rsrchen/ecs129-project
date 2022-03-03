import sys

print("Number of arguments:", len(sys.argv), "arguments.")
print("Argument List:", str(sys.argv))

"""
so. how's it gonna be?

default settings:
accept one sequence only
ask for 4 character PDB ID code and force user to enter, else exit
directory containing PDB file is ./pdb_files
directory containing coordinate files (seq1rank1 thru seq1goldstandard) is ./coordinate_files

changeable settings:
# of sequences to do rmsd shit for
PDB files directory
coords txt files directory

steps:
1. look at alphafold's predictions and generate 5 pdb files of only alpha carbons
1.5. add spaces where they ought to be
2. generate alpha carbon coords plaintext file from that ^ and put it in coordinate files (goodbye awk. it'll be too hard for me to reach into the WSL via python. i'll have to code this myself.)
3. read that coordinate file and do the rmsd shit!
4. repeat for all the sequences the user inputs

"""