def add_spaces(filename: str):
    lines = []
    with open(filename, "r", encoding="utf8") as file_whose_coords_we_gotta_space_out:
        for line in file_whose_coords_we_gotta_space_out:
            lines.append(line)
    for line in lines:
        print(line, end="")
        # recognize the pattern of "digit followed by minus" via regex
        
    # with open(filename.split(".")[0] + "_spaced_coords.pdb", "w") as spaced_out_file:
    #     write_string = ""
    #     for line in lines: 
    #         write_string += line
    #     spaced_out_file.write(write_string)


add_spaces("4x96_out.pdb")
