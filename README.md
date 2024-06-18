# ECS 129 Winter Quarter 2022 Project - Protein Structure Comparison Program

- [ECS 129 Winter Quarter 2022 Project - Protein Structure Comparison Program](#ecs-129-winter-quarter-2022-project---protein-structure-comparison-program)
  - [What](#what)
  - [More what](#more-what)
  - [How](#how)
  - [Why](#why)
  - [Who](#who)
  - [Report](#report)


## What 
This program takes a set of multiple protein structures, where each protein structure is given by a text file containing the (x, y, z) coordinates of the protein's alpha carbons, and compares all of the structures to one another by calculating the root-mean-square deviation, or RMSD, between pairs of structures.

## More what
The program functions via CLI. It takes five protein structure predictions (the default number generated by AlphaFold) and one experimentally determined structure (as empirically derived from crystallography or cryo-EM). The program displays a heatmap generated from the RMSDs of all comparisons of all protein structures and a bar graph illustrating how the protein structure predictions stack up against one another when compared to the experimentally-determined structure. 

## How
We use the quaternion-based RMSD algorithm provided by Coutsias, Seok, and Dill in [this paper](https://www.cs.ucdavis.edu/~koehl/Teaching/ECS129/Projects/Coutsias_2004.pdf). We also use the open-source community packages [numpy](https://numpy.org/) and [matplotlib](https://matplotlib.org/). 

## Why
Protein structure prediction has been a huge area of research for decades. Recently, it's been all over the news. For instance, AlphaFold recently went on display at CASP, the major biannual research competition dedicated to 3D protein structure work, and [and](https://www.science.org/content/article/google-s-deepmind-aces-protein-folding) [has](https://www.theguardian.com/science/2018/dec/02/google-deepminds-ai-program-alphafold-predicts-3d-shapes-of-proteins) [been](https://www.nytimes.com/2019/02/05/technology/artificial-intelligence-drug-research-deepmind.html) [making](https://www.forbes.com/sites/samshead/2018/12/03/deepmind-starts-to-show-how-ai-can-be-used-to-solve-scientific-problems/?sh=46c3570be1e2) [headlines](https://www.youtube.com/watch?v=gVzPMZqOTo4). We chose to make this topic the focus of our ECS 129 project and write a program that evaluates the validity of a protein structure prediction by comparing it to the empirically-determined true structure.

## Who
- **Raymond Chen** - programming, debugging, refactoring, report writing, writing this readme
- **Emily Cheng** - programming, report writing
- **Daniel Cardenas** - programming, report writing

## Report
A report on this program was prepared for *ECS 129 - Computational Structural Bioinformatics* taught by [Patrice Koehl](https://www.cs.ucdavis.edu/~koehl/index.html). It can be found [here](https://drive.google.com/file/d/1XDiJW5NY0E51er4A13-ZF6D0C4YYL105/view?usp=sharing). 

*This report was written when the project was in a different state than it is now, before I merged my own branch containing my own individual work with the master branch, so some stuff (such as the presence of the CLI) might be different.*
