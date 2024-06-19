# ECS 129 Winter Quarter 2022 Project - Protein Structure Comparison Program

- [ECS 129 Winter Quarter 2022 Project - Protein Structure Comparison Program](#ecs-129-winter-quarter-2022-project---protein-structure-comparison-program)
  - [What](#what)
  - [What, continued](#what-continued)
  - [Why](#why)
  - [Who](#who)
  - [Report](#report)
- [how to use](#how-to-use)
  - [the main program (`command_line.py`)](#the-main-program-command_linepy)
    - [flags and arguments](#flags-and-arguments)
    - [example usage](#example-usage)
  - [pdb length finder](#pdb-length-finder)
    - [flags and arguments](#flags-and-arguments-1)
    - [example usage](#example-usage-1)

## What 
This program uses the quaternion-based root-mean-square deviation algorithm from "Using Quaternions to Calculate RMSD" by Coutsias, Seok, and Dill (2004) to compare a set of protein structures to one another.

## What, continued
This command-line utility takes five protein structure predictions (the default number of structures generated by AlphaFold) and one experimentally determined structure (as empirically derived from crystallography, cryo-EM, or other means) and evaluates their structural similarity with regards to one another using the root-mean-square deviations between the alpha carbons of different structures. 

The program displays a heatmap generated from the root-mean-square deviations of all comparisons of all protein structures and a bar graph illustrating how the protein structure predictions stack up against one another when compared to the experimentally-determined structure. 

This program was written in Python and relies on [numpy](https://numpy.org/) and [matplotlib](https://matplotlib.org/), among other dependencies. These are listed in `requirements.txt`.

## Why
Protein structure prediction has been a huge area of research for decades, and as of late, it's been all over the news. For instance, AlphaFold recently went on display at CASP, the major biannual research competition dedicated to 3D protein structure work, and [and](https://www.science.org/content/article/google-s-deepmind-aces-protein-folding) [has](https://www.theguardian.com/science/2018/dec/02/google-deepminds-ai-program-alphafold-predicts-3d-shapes-of-proteins) [been](https://www.nytimes.com/2019/02/05/technology/artificial-intelligence-drug-research-deepmind.html) [making](https://www.forbes.com/sites/samshead/2018/12/03/deepmind-starts-to-show-how-ai-can-be-used-to-solve-scientific-problems/?sh=46c3570be1e2) [headlines](https://www.youtube.com/watch?v=gVzPMZqOTo4). We chose to make this topic the focus of our ECS 129 project and write a program that evaluates the validity of a protein structure prediction by comparing it to the empirically-determined true structure.

## Who
- **Raymond Chen** - programming, debugging, refactoring, report writing, additional improvements
- **Emily Cheng** - programming, report writing
- **Daniel Cardenas** - programming, report writing

## Report
A report on this program was prepared for *ECS 129 - Computational Structural Bioinformatics* taught by [Patrice Koehl](https://www.cs.ucdavis.edu/~koehl/index.html). It can be found [here](https://drive.google.com/file/d/1XDiJW5NY0E51er4A13-ZF6D0C4YYL105/view?usp=sharing). 

*This report was written when the project was in a different state than it is now, before I merged my own branch containing my own individual work with the master branch, so some stuff (such as the presence of the CLI) might be different.*

# how to use
Open up your shell of choice and follow the instructions below.

## the main program (`command_line.py`)

This is the entry point of the main program. Use the CLI (command-line interface) to interact with the program and calculate the root-mean-square deviation between alpha carbons in your structures of interest. 

### flags and arguments
- `-a`, the directory that contains AlphaFold's predictions in the form of PDB files. By default, it is `./structures/alphafold_predictions`.
- `-c`, which protein chains of the predicted structures you want to examine. By default, it's just chain A. You can input `AB` if you want the program to read chains A and B, or `ABCD` for chains A, B, C, and D. 
- `-C`, which protein chains of the solved structure you want to examine. Similar to `-c`.
- `-h`, **required**, the hash value assigned to your AlphaFold predictions by ColabFold.
- `-p`, **required**, the PDB ID of your solved structure.
- `-s`, the directory that contains the solved structures. These are the experimentally determined structures, solved using x-ray crystallography or cryo-EM or similar methods. By default, it is `./structures/solved_structures`.

### example usage
I type this command into my shell:
`python .\command_line.py -p 1grq -h b2b87 `

The first word calls my python executable. 

The second word is the entry point of the program, a python file called `command_line.py`. 

Then, some flags and arguments. 
1. `-p 1grq` tells the program that the PDB ID of the solved protein structure is 1GRQ. This is the PDB file for the solved structure of [CHLORAMPHENICOL PHOSPHOTRANSFERASE IN COMPLEX WITH P-AMINO-CHLORAMPHENICOL FROM STREPTOMYCES VENEZUELAE](https://www.rcsb.org/structure/1GRQ).
2. `-h b2b87` tells the program that the ColabFold hash is b2b87. When I used ColabFold to predict how this protein would fold, it gave me a jobname and attached a hash value to it. All the PDB files of AlphaFold's structure predictions now have this hash value, b2b87, in their filenames. The program will use this hash value to discern which structure predictions are of the same protein. 
3. You'll notice there's no `-s`, `-a`, `-c`, or `-C`. The program will use the default values for the solved structures directory, AlphaFold predictions directory, chains of the predicted structure to examine, and chains of the solved structure to examine.

The program will run and print some comparison stats to the shell, as well as display a heatmap and bar graph visualizing the data.

Here's the output.

```
The (New and Improved) ECS 129 Protein Structure Comparison Program. © 2022-20XX rsrchen (github.com/rsrchen)

No argument provided for -a; default predicted structures directory (./structures/alphafold_predictions) will be used.
No argument provided for -s; default solved structures directory (./structures/solved_structures) will be used.
No argument provided for -c; default chain A will be used.
No argument provided for -C; default chain A will be used.
1grq_rank1 and 1grq_rank1 RMSD: 0.0099
1grq_rank1 and 1grq_rank2 RMSD: 0.188
1grq_rank1 and 1grq_rank3 RMSD: 0.2099
1grq_rank1 and 1grq_rank4 RMSD: 0.2562
1grq_rank1 and 1grq_rank5 RMSD: 0.1959
1grq_rank1 and 1grq_goldstandard RMSD: 0.639
1grq_rank2 and 1grq_rank1 RMSD: 0.188
1grq_rank2 and 1grq_rank2 RMSD: 0.0047
1grq_rank2 and 1grq_rank3 RMSD: 0.1231
1grq_rank2 and 1grq_rank4 RMSD: 0.2149
1grq_rank2 and 1grq_rank5 RMSD: 0.206
1grq_rank2 and 1grq_goldstandard RMSD: 0.5896
1grq_rank3 and 1grq_rank1 RMSD: 0.2099
1grq_rank3 and 1grq_rank2 RMSD: 0.1231
1grq_rank3 and 1grq_rank3 RMSD: 0.0047
1grq_rank3 and 1grq_rank4 RMSD: 0.2239
1grq_rank3 and 1grq_rank5 RMSD: 0.2126
1grq_rank3 and 1grq_goldstandard RMSD: 0.58
1grq_rank4 and 1grq_rank1 RMSD: 0.2562
1grq_rank4 and 1grq_rank2 RMSD: 0.2149
1grq_rank4 and 1grq_rank3 RMSD: 0.2239
1grq_rank4 and 1grq_rank4 RMSD: 0.0081
1grq_rank4 and 1grq_rank5 RMSD: 0.1754
1grq_rank4 and 1grq_goldstandard RMSD: 0.6273
1grq_rank5 and 1grq_rank1 RMSD: 0.1959
1grq_rank5 and 1grq_rank2 RMSD: 0.206
1grq_rank5 and 1grq_rank3 RMSD: 0.2126
1grq_rank5 and 1grq_rank4 RMSD: 0.1754
1grq_rank5 and 1grq_rank5 RMSD: 0.0166
1grq_rank5 and 1grq_goldstandard RMSD: 0.6342
1grq_goldstandard and 1grq_rank1 RMSD: 0.639
1grq_goldstandard and 1grq_rank2 RMSD: 0.5896
1grq_goldstandard and 1grq_rank3 RMSD: 0.58
1grq_goldstandard and 1grq_rank4 RMSD: 0.6273
1grq_goldstandard and 1grq_rank5 RMSD: 0.6342
1grq_goldstandard and 1grq_goldstandard RMSD: 0.011
```

![output plots](/info_md_assets/1.png)

One more example:

`python .\command_line.py -p 1czd -h df4c0 -c b -C a -a new-directory/some-subdirectory -s new-directory`

A few things are different from the previous example.
1. The PDB ID and hash values are different; I'm looking at [CRYSTAL STRUCTURE OF THE PROCESSIVITY CLAMP GP45 FROM BACTERIOPHAGE T4](https://www.rcsb.org/structure/1CZD) this time.
2. `-c b` is used to specify that the program should look at chain B of the predicted structure.
3. `-C a` is used to specify that the program should look at chain A of the solved structure. 
4. `-a` and `-s` are used to specify that the program should search in the `./new-directory/some-subdirectory` and `./new-directory` paths to find the predicted structure and solved structure files, respectively.

Here's the output.

```
The (New and Improved) ECS 129 Protein Structure Comparison Program. © 2022-20XX rsrchen (github.com/rsrchen)

1czd_rank1 and 1czd_rank1 RMSD: 0.0041
1czd_rank1 and 1czd_rank2 RMSD: 0.1409
1czd_rank1 and 1czd_rank3 RMSD: 0.1101
1czd_rank1 and 1czd_rank4 RMSD: 0.1227
1czd_rank1 and 1czd_rank5 RMSD: 0.212
1czd_rank1 and 1czd_goldstandard RMSD: 0.6979
1czd_rank2 and 1czd_rank1 RMSD: 0.1409
1czd_rank2 and 1czd_rank2 RMSD: 0.019
1czd_rank2 and 1czd_rank3 RMSD: 0.1064
1czd_rank2 and 1czd_rank4 RMSD: 0.1256
1czd_rank2 and 1czd_rank5 RMSD: 0.2199
1czd_rank2 and 1czd_goldstandard RMSD: 0.6843
1czd_rank3 and 1czd_rank1 RMSD: 0.1101
1czd_rank3 and 1czd_rank2 RMSD: 0.1064
1czd_rank3 and 1czd_rank3 RMSD: 0.016
1czd_rank3 and 1czd_rank4 RMSD: 0.1243
1czd_rank3 and 1czd_rank5 RMSD: 0.1768
1czd_rank3 and 1czd_goldstandard RMSD: 0.6854
1czd_rank4 and 1czd_rank1 RMSD: 0.1227
1czd_rank4 and 1czd_rank2 RMSD: 0.1256
1czd_rank4 and 1czd_rank3 RMSD: 0.1243
1czd_rank4 and 1czd_rank4 RMSD: 0.0072
1czd_rank4 and 1czd_rank5 RMSD: 0.2341
1czd_rank4 and 1czd_goldstandard RMSD: 0.7056
1czd_rank5 and 1czd_rank1 RMSD: 0.212
1czd_rank5 and 1czd_rank2 RMSD: 0.2199
1czd_rank5 and 1czd_rank3 RMSD: 0.1768
1czd_rank5 and 1czd_rank4 RMSD: 0.2341
1czd_rank5 and 1czd_rank5 RMSD: 0.0155
1czd_rank5 and 1czd_goldstandard RMSD: 0.7256
1czd_goldstandard and 1czd_rank1 RMSD: 0.6979
1czd_goldstandard and 1czd_rank2 RMSD: 0.6843
1czd_goldstandard and 1czd_rank3 RMSD: 0.6854
1czd_goldstandard and 1czd_rank4 RMSD: 0.7056
1czd_goldstandard and 1czd_rank5 RMSD: 0.7256
1czd_goldstandard and 1czd_goldstandard RMSD: 0.0106
```

![output plots](/info_md_assets/2.png)

## pdb length finder

This is an additional utility you can use to find the length of a particular protein sequence.

### flags and arguments
- `-n`, **required**, the name of the file.
- `-c`, which protein chains you want to measure the length of.

### example usage
I type this command into my shell:
`python .\pdb_length_finder.py -n 1a2y.pdb -c ab`

1. I use `-n` to indicate the name of the file. That's `1a2y.pdb`.
2. I use `-c` to indicate the chains I want to measure the length of, chains A and B.

Here's the output. 

```
PDB File Length Finder

Length of sequence specified: 223
```