# ECS 129 Winter Quarter 2022 Project - Protein Structure Comparison Program

- [ECS 129 Winter Quarter 2022 Project - Protein Structure Comparison Program](#ecs-129-winter-quarter-2022-project---protein-structure-comparison-program)
  - [What](#what)
  - [More what](#more-what)
  - [How](#how)
  - [Why](#why)
  - [Who](#who)
  - [Report](#report)


## What 
This program takes a set of multiple protein structures, where each protein structure is given by a text file containing the (x, y, z) coordinates of the protein's alpha carbons, and compares all of the structures to one another by calculating the root-mean-square deviation, or RMSD, between pairs of structures. Pretty cool.

## More what
The program functions via CLI. It takes five protein structure predictions (i.e. from AlphaFold) and one experimentally determined structure (i.e. as empirically derived from crystallography or cryo-EM). The program also shows you a heatmap generated from the RMSDs of all comparisons of all protein structures and serves you a bar graph giving you a closer look at how the protein structure predictions stack up against one another when compared to the experimentally-determined structure. 

## How
We use the quaternion-based RMSD algorithm provided by Coutsias, Seok, and Dill in [this paper](https://www.cs.ucdavis.edu/~koehl/Teaching/ECS129/Projects/Coutsias_2004.pdf). We also graciously use the open-source community packages [numpy](https://numpy.org/) and [matplotlib](https://matplotlib.org/). Thanks. We love you.

## Why
The science around protein structure prediction is, and has for decades been, absolutely booming. People around the globe are working on computational methods for protein structure prediction day in and day out. You've heard about CASP, the major biannual research competition dedicated to 3D protein structure work. You've heard about AlphaFold, the major recent breakthrough in structure prediction. [Everyone's](https://www.science.org/content/article/google-s-deepmind-aces-protein-folding) [talking](https://www.theguardian.com/science/2018/dec/02/google-deepminds-ai-program-alphafold-predicts-3d-shapes-of-proteins) [about](https://www.nytimes.com/2019/02/05/technology/artificial-intelligence-drug-research-deepmind.html) [this](https://www.forbes.com/sites/samshead/2018/12/03/deepmind-starts-to-show-how-ai-can-be-used-to-solve-scientific-problems/?sh=46c3570be1e2) [stuff](https://www.youtube.com/watch?v=gVzPMZqOTo4). It's changing the future. The point is—it's a huge area of research, and it's incredibly interesting. That's why we chose to focus on it for our ECS 129 project and write a program that evaluates just how good a protein structure prediction really is by comparing it to the empirically-determined true structure.

## Who
- **Raymond Chen** - programming, debugging, refactoring, report writing, writing this readme
- **Emily Cheng** - programming, report writing
- **Daniel Cardenas** - programming, report writing

## Report
You may have noticed credit for "report writing" in the previous section. We wrote a report on this program for ECS 129 - Computational Structural Bioinformatics. Took the class winter quarter 2022 with [Professor Patrice Koehl](https://www.cs.ucdavis.edu/~koehl/index.html), who I think is a great person and a very passionate instructor. Here's a link to [the original report](https://drive.google.com/file/d/1XDiJW5NY0E51er4A13-ZF6D0C4YYL105/view?usp=sharing). 
