# How to use???

I've just given this program a CLI. Spent all of last night coding it. *For fun.* What am I doing with my life? It's not even like anyone's going to use this program anyway.

Anyway, for folks unfamiliar with what I'm talking about, a CLI (command-line interface) works as follows: you pull up a command terminal, you execute this program with python, and you add flags and arguments to specify how exactly you want the program to run.

So go to cmd, or PowerShell, or bash, or zsh, or Apple Terminal and get to typing!

## Flags and Arguments
- -a, the directory that contains AlphaFold's predictions in the form of PDB files. By default, it is `./alphafold_predictions`.
- -c, which protein chains of the solved structure you want to compare the predictions to. By default, it's just the A chain, `A`. You can input `AB` or `BA` if you want the program to read chains A and B of the solved structure, `ABCD` or `CDBA` or `AACBDDBCBD` if you want it to look at chains A, B, C, and D, you get the picture. Note that if you write `ABC` and the structure only contains two chains named A and B, everything will still work just fine! 
- -h, the hash value assigned to your AlphaFold predictions by ColabFold. It's a 5 character value that consists of letters and numbers. ColabFold gives you one every time you use it to make structure predictions. You need to enter this; else the program won't run.
- -p, the PDB ID of your solved structure. You need to enter this; else the program won't run.
- -s, the directory that contains the solved structures. These are the experimentally determined structures, solved using x-ray crystallography or cryo-EM or something along those lines. By default, it is `./solved_structures`.

## Example usage
I type this command into PowerShell:
`C:/path/to/your/python/installation/python.exe "c:/path/to/this/program/THE PROJECT/command_line.py" -p 7q4m -h 405fa`

The first word is the path to my python executable. This is a python program, after all. I need to use the python interpreter to make sense of it. 

The second word is the entry point of the program, a python file called `command_line.py`. You need to start here.

Then we've got a couple of flags and arguments. 
1. `-p 7q4m` tells the program that the PDB ID of the solved protein structure is 7Q4M. This PDB ID is for real, dawg. You can go to the PDB and find that we're looking at [Type II beta-amyloid 42 filaments from the human brain](https://www.rcsb.org/structure/7Q4M).
2. `-h 405fa` tells the program that the ColabFold hash is 405fa. When I used ColabFold to predict how this protein would fold, it gave me a jobname and attached a hash value to it. All the PDB files of AlphaFold's structure predictions now have this hash value, 405fa, in their filenames. The program will use this hash value to discern which structure predictions are of the same protein. It's important. 
3. You'll notice there's no `-s`, `-a`, or `-c`. I'm letting the program proceed with the default values for all of that stuff.

And that's that! 