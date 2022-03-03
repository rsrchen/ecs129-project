from pathlib import Path
import awk_but_not_really


def execute():
    a = "pdb_files"
    p = Path("./")
    alphafold_prediction_pdb_files = p.glob(a + "/*.pdb")
    [
        # awk_but_not_really.create_coordinates_text_file(x, "1ab1")
        print(x)
        for x in alphafold_prediction_pdb_files
    ]
    # return name_of_clean_well_spaced_pdb_file


execute()
