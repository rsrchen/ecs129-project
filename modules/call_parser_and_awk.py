from pathlib import Path
from time import sleep
import awk_but_not_really
import parse_pdb


def execute():
    a = "pdb_files"
    p = Path("./")
    alphafold_prediction_pdb_files = p.glob(a + "/*.pdb")
    [
        parse_pdb.get_alpha_carbons(x, "1ab1")
        for x in alphafold_prediction_pdb_files
    ]
    sleep(1)
    [
        awk_but_not_really.create_coordinates_text_file(x, "1ab1")
        for x in alphafold_prediction_pdb_files
    ]
    # return name_of_clean_well_spaced_pdb_file


execute()
