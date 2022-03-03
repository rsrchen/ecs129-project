from pathlib import Path
import asyncio
import awk_but_not_really
import parse_pdb


async def execute():
    a = "pdb_files"
    p = Path("./")
    alphafold_prediction_pdb_files = p.glob(a + "/*.pdb")
    [
        parse_pdb.get_alpha_carbons(x, "1ab1")
        for x in alphafold_prediction_pdb_files
    ]
    
    [
        awk_but_not_really.create_coordinates_text_file(x, "1ab1")
        for x in alphafold_prediction_pdb_files
    ]
    # return name_of_clean_well_spaced_pdb_file


asyncio.run(execute())
