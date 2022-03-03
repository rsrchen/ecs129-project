import regex


def add_space_regex_shit(match_object):
    return str(match_object.group(0)[0] + " " + match_object.group(0)[1:])


def add_spaces(filename: str):
    lines = []
    with open(filename, "r", encoding="utf8") as file_whose_coords_we_gotta_space_out:
        for line in file_whose_coords_we_gotta_space_out:
            lines.append(line)
    with open(filename.split(".pdb")[0] + "_spaced_coords.pdb", "w") as spaced_out_file:
        write_string = ""
        for line in lines:
            # recognize the pattern of "digit followed by minus" via regex
            search: list[str] = regex.findall(r"\d-\d", line)
            if search:
                # if we get a match, aka if there's a digit then a
                # minus then a digit (BAD NO SPACE VERY BAD)
                # for each found number dash number, substitute their occurrences in the line with themselves but spaced out.

                line = regex.sub(r"\d-\d", add_space_regex_shit, line)
                # search_for_nospace = regex.search(search[i])
                # line = (
                #     line[: search_for_nospace.start() + 1]
                #     + " "
                #     + line[search_for_nospace.end() - 2 :]
                # )
            write_string += line
        spaced_out_file.write(write_string)


add_spaces("4x96_out.pdb")
