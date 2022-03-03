from textwrap import wrap
import numpy as np
import math
import matplotlib.pyplot as plt
from textwrap import wrap


def generate(dictionary_of_RMSDs: dict[str, float]):
    """
    Given a dictionary of RMSDs comparing AlphaFold predictions to
    experimentally-determined structures, generate 1 color-coded heatmap
    that compares all of the RMSDs to one another, and 1 log-scale bar graph
    that compares only the RMSDs of the predicted structures to the RMSD of
    the experimentally-determined structure.

    """
    # the plan: take all the keys and decompose them to get individual tokens. seq1rank1, seq1rank2, etc. then put them into a set. loop through the values and populate a 2D array with them.

    structure_names: set[str] = {""}
    array_side_size = int(math.sqrt(len(dictionary_of_RMSDs)))
    rmsd_array = np.zeros((array_side_size, array_side_size))
    row = -1
    col = 0
    old = ""
    for key, value in dictionary_of_RMSDs.items():
        tokens = key.split(" and ")
        structure_names.add(tokens[0])
        if tokens[0] != old and row < 6:
            row += 1
            col = 0
            old = tokens[0]
            if row == 6:
                row = 0
        rmsd_array[row][col] = value
        col += 1
    structure_names.remove("")
    structure_names_list = sorted(structure_names)
    structure_names_list.append(structure_names_list[0])
    structure_names_list.remove(structure_names_list[0])

    # here's where the plotting begins
    fig, ax = plt.subplots(ncols=2, figsize=(14, 9))
    plt.tight_layout(pad=10)
    ax[0].imshow(rmsd_array, cmap="RdPu")
    ax[0].set_title(
        "\n".join(
            wrap(
                "A Comparison Heatmap Between the Root-Mean-Square Deviations Of AlphaFold Structure Predictions and the Experimentally Determined Protein Structure",
                70,
            )
        )
    )
    ax[0].set_xticks(range(array_side_size), labels=structure_names_list)
    ax[0].set_yticks(range(array_side_size), labels=structure_names_list)
    ax[0].set_xlabel(
        "Each tick is labeled with the name we have given the structure, \nwhich consists of its corresponding sequence (e.g. seq1) and \nits rank, as ranked by AlphaFold (e.g. rank3). The experimentally \ndetermined structure is given the name 'goldstandard.' ",
        labelpad=10,
    )
    plt.setp(ax[0].get_xticklabels(), rotation=20, ha="right", rotation_mode="anchor")

    for i in range(array_side_size):
        for j in range(array_side_size):
            ax[0].text(j, i, rmsd_array[i][j], ha="center", va="center", color="green")

    rmsd_array_goldstandard = rmsd_array[-1][:-1]
    ax[1].bar(range(array_side_size - 1), rmsd_array_goldstandard, color="magenta")
    ax[1].set_title(
        "\n".join(
            wrap(
                "Root-Mean-Square Deviation Comparisons Between Each AlphaFold Prediction and the Experimentally Determined Structure Only",
                70,
            )
        )
    )
    ax[1].set_xticks(range(array_side_size - 1), labels=structure_names_list[:-1])
    ax[1].set_yticks(
        np.arange(
            int(max(rmsd_array_goldstandard) - (max(rmsd_array_goldstandard) * 0.2)),
            (int(max(rmsd_array_goldstandard + (max(rmsd_array_goldstandard) * 0.2)))),
            0.1 * max(rmsd_array_goldstandard),
        )
    )
    ax[1].set_yscale("log")
    ax[1].set_xlabel("Name and Rank of Structure Prediction", labelpad=20)
    ax[1].set_ylabel("Root-Mean-Square Deviation", labelpad=20)

    # and voila!
    plt.show()

    pass
