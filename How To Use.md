# How to use
Open up your shell of choice and follow the instructions below.

## the main program (`command_line.py`)

This is the entry point of the main program. Use the CLI (command-line interface) to interact with the program and calculate the root-mean-square deviation between alpha carbons in your structures of interest. 

### Flags and Arguments
- `-a`, the directory that contains AlphaFold's predictions in the form of PDB files. By default, it is `./structures/alphafold_predictions`.
- `-c`, which protein chains of the solved structure you want to compare the predictions to. By default, it's just chain A, `A`. You can input `AB` if you want the program to read chains A and B of the solved structure, or `ABCD` for chains A, B, C, and D. 
- `-h`, **required**, the hash value assigned to your AlphaFold predictions by ColabFold.
- `-p`, **required**, the PDB ID of your solved structure.
- `-s`, the directory that contains the solved structures. These are the experimentally determined structures, solved using x-ray crystallography or cryo-EM or similar methods. By default, it is `./structures/solved_structures`.

### Example usage
I type this command into my shell:
`python .\command_line.py -p 1grq -h b2b87 `

The first word calls my python executable. 

The second word is the entry point of the program, a python file called `command_line.py`. 

Then, some flags and arguments. 
1. `-p 1grq` tells the program that the PDB ID of the solved protein structure is 1GRQ. This is the PDB file for the solved structure of [CHLORAMPHENICOL PHOSPHOTRANSFERASE IN COMPLEX WITH P-AMINO-CHLORAMPHENICOL FROM STREPTOMYCES VENEZUELAE](https://www.rcsb.org/structure/1GRQ).
2. `-h b2b87` tells the program that the ColabFold hash is b2b87. When I used ColabFold to predict how this protein would fold, it gave me a jobname and attached a hash value to it. All the PDB files of AlphaFold's structure predictions now have this hash value, b2b87, in their filenames. The program will use this hash value to discern which structure predictions are of the same protein. It's important. 
3. You'll notice there's no `-s`, `-a`, or `-c`. The program will use the default values for the solved structures directory, AlphaFold predictions directory, and chains to examine.

The program will run and print some comparison stats to the shell, as well as display a heatmap and bar graph visualizing the data.

Here's the output.

```
The (New and Improved) ECS 129 Protein Structure Comparison Program. © 2022 rsrchen (github.com/rsrchen)

No argument provided for -a; default predicted structures directory (./structures/alphafold_predictions) will be used.
No argument provided for -s; default solved structures directory (./structures/solved_structures) will be used.
No argument provided for -c; default chain A will be used.
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

## pdb length finder

This is an additional utility you can use to find the length of a particular protein sequence.

### Flags and Arguments
- `-n`, **required**, the name of the file.
- `-c`, which protein chains you want to measure the length of.

### Example usage
I type this command into my shell:
`python .\pdb_length_finder.py -n 1a2y.pdb -c ab`

1. I use `-n` to indicate the name of the file. That's `1a2y.pdb`.
2. I use `-c` to indicate the chains I want to measure the length of, chains A and B.

Here's the output. 

```
PDB File Length Finder

Length of sequence specified: 223
```