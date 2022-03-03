import sys

print("Number of arguments:", len(sys.argv), "arguments.")
print("Argument List:", str(sys.argv))

"""
so. how's it gonna be?

default settings:
accept one sequence only
accept 4 character PDB ID code, else exit
directory containing PDB files is ./pdb_files
directory containing coordinate files (seq1rank1 thru seq1goldstandard) is ./coordinate_files

changeable settings:
# of sequences to do rmsd shit for
PDB files directory
coords txt files directory

overview:
1. look at alphafold's predictions and generate 5 pdb files of only alpha carbons
1.5. add spaces where they ought to be
2. generate alpha carbon coords plaintext file from that ^ and put it in coordinate files (goodbye awk. it'll be too hard for me to reach into the WSL via python. i'll have to code this myself.)
3. read that coordinate file and do the rmsd shit!
4. repeat for all the sequences the user inputs

notes that go a bit further in depth
i download the pdb file for the gold standard from the internet, generate an alpha carbon text file using parse_pdb, then use awk on it to generate a text file containing only the coords of the alpha carbons.
i put a sequence into colabfold. they give me a folder with 5 structure predictions. these are PDB files. i take these pdb files and generate alpha carbon text files using parse_pdb, then awk them to generate a text file containing only the coords of the CA atoms
i'll ask the user for the directory of the alphafold predictions.
i need to learn how to do async shit in python 


"""