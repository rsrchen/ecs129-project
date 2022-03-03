import sys

print("Number of arguments:", len(sys.argv), "arguments.")
print("Argument List:", str(sys.argv))

"""
so. how's it gonna be?

default settings:
accept one sequence only
accept 4 character PDB ID code, else exit
directory containing PDB files is ./pdb_files

changeable settings:
# of sequences to accept
PDB files directory

overview:
1. read pdb files of alphafold's structure predictions 
2. get alpha carbon coordinates
3. 


"""

# -p is the flag people will use to indicate PDB files directory
if "-p" in sys.argv:
    print('p')
