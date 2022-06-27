from pathlib import Path


def create_coordinates_text_file(filename: str | Path, pdb_id: str):
    output_string = ""
    with open(filename) as pdb_file:
        for line in pdb_file:
            line = line.split()
            #  awk '{if($3=="CA" && $1=="ATOM") print $7 " " $8 " " $9}' test_405fa_unrelaxed_rank_5_model_5.pdb > 7q4mrank5.txt
            if len(line) > 2 and line[2] == "CA" and line[0] == "ATOM":
                output_string += line[6] + " " + line[7] + " " + line[8] + "\n"
    for i in range(1, 6):
        with open("coordinate_files/" + pdb_id + "_rank" + str(i) + ".pdb", "w") as write_file:
            write_file.write(output_string)
