from pathlib import Path
from awk_but_not_really import create_coordinates_text_file


def execute():
    a = "pdb_files"
    p = Path("./")
    alphafold_prediction_pdb_files = p.glob(a + "/*.pdb")
    [print(x) for x in alphafold_prediction_pdb_files]
    # return name_of_clean_well_spaced_pdb_file

execute()

# create_coordinates_text_file("test_3aafb_unrelaxed", "1ab1")
