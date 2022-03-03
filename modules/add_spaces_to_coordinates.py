import regex


def add_spaces(filename: str):
    lines = []
    with open(filename, "r", encoding="utf8") as file_whose_coords_we_gotta_space_out:
        for line in file_whose_coords_we_gotta_space_out:
            lines.append(line)
    with open(filename.split(".")[0] + "_spaced_coords.pdb", "w") as spaced_out_file:
        write_string = ""
        for line in lines:
            # recognize the pattern of "digit followed by minus" via regex
            search = regex.search(r"\d-\d", line)
            if (
                search
            ):  # if we get a match, aka if there's a digit then a minus then a digit (BAD NO SPACE VERY BAD)
                line = line[: search.start() + 1] + " " + line[search.end() - 2 :]
            write_string += line
        spaced_out_file.write(write_string)


add_spaces("4x96_out.pdb")
