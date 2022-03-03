from pathlib import Path
from unicodedata import name
from Bio.PDB import PDBParser
from Bio.PDB import PDBIO

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
    if use_chains:
        [
            alpha_carbon_coords.append(atom.coord)
            for atom in protein_atoms
            if atom.name == "CA" and atom.get_full_id()[2] in chains
        ]
    else:
        [
            alpha_carbon_coords.append(atom.coord)
            for atom in protein_atoms
            if atom.name == "CA"
        ]
    return alpha_carbon_coords
    # pdb_io.set_structure(protein)

    # pdb_io.save((str(filename).split(".pdb")[0]) + "_alpha_carbons.pdb", AlphaCarbonSelect())
