from Bio.PDB import PDBParser
from Bio.PDB import PDBIO


class Select:
    def accept_model(self, model):
        return 1

    def accept_chain(self, chain):
        return 1

    def accept_residue(self, residue):
        return 1

    def accept_atom(self, atom):
        print("atom id:" + atom.get_id())
        print("atom name:" + atom.get_name())
        if atom.get_name() == "CA":
            print("True")
            return 1
        else:
            return 0


def get_alpha_carbons():
    pdb_parser = PDBParser()
    pdb_io = PDBIO()
    protein_1ab1 = pdb_parser.get_structure(id="1ab1", file="1ab1.pdb")
    pdb_io.set_structure(protein_1ab1)
    pdb_io.save("1ab1_out.pdb", Select())
    pass


get_alpha_carbons()
pass
