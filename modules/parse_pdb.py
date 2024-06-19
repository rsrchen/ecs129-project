from pathlib import Path
from unicodedata import name
from Bio.PDB import PDBParser
from Bio.PDB import parse_pdb_header

# from Bio.PDB import PDBIO

# from Bio.SeqUtils import seq1
from Bio.PDB.PDBIO import Select


class AlphaCarbonSelect(Select):
    def accept_model(self, model):
        return 1

    def accept_chain(self, chain):
        return 1

    def accept_residue(self, residue):
        # print(seq1(residue.get_resname()), end="")
        return 1

    def accept_atom(self, atom):
        # print("atom id:" + atom.get_id())
        # print("atom name:" + atom.get_name())
        if atom.get_name() == "CA":
            # print("True")
            return 1
        else:
            return 0


def get_alpha_carbons(
    filename: str | Path, pdb_id: str, chains: str, use_chains: bool = False
):
    pdb_parser = PDBParser(QUIET=True)
    # pdb_io = PDBIO()
    protein = pdb_parser.get_structure(id=pdb_id, file=filename)
    protein_atoms = protein.get_atoms()
    alpha_carbon_coords = []
    if (
        use_chains
    ):  # reading a solved structure file where only certain chains are wanted
        # i need to change this.
        # changed plan below.
        # use chains if reading either a solved structure file or a structure prediction. 
        '''
        pt 1
        i need to have the user specify chains for the solved structure AND for the prediction.
        so like 
        python .\command_line.py -p 1a3q -h 9a9da -c bc -C ab
        -c will be chains of the prediction 
        -C will be chains of the solved structure 

        then this function of this module, get alpha carbons, gets to be the same. no changes here
        i'll just need to alter how and when i call it. 

        go to set_up_coord_files.py for pt 2
        '''
        [
            alpha_carbon_coords.append(atom.coord)
            for atom in protein_atoms
            if atom.name == "CA"
            and atom.element == "C"
            and atom.get_full_id()[2] in chains
        ]
    else:  # reading a structure prediction file where all chains are wanted
        [
            alpha_carbon_coords.append(atom.coord)
            for atom in protein_atoms
            if atom.name == "CA" and atom.element == "C"
        ]
    header = parse_pdb_header(filename)
    if header["has_missing_residues"]:
        alpha_carbon_coords = [-1]
    return alpha_carbon_coords
    # pdb_io.set_structure(protein)

    # pdb_io.save((str(filename).split(".pdb")[0]) + "_alpha_carbons.pdb", AlphaCarbonSelect())
