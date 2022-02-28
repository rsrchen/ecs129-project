# ECS 129 Midterm Project Outline
Not sure how to do this. But we're giving it a shot anyway

## What to do: 
1. Run AlphaFold to predict the structures of the two proteins given in the prompt (Fimbrial adhesin from Proteus mirabilis, which we'll refer to as sequence 1, and CST complex unit CTC1, which we'll refer to as sequence 2)
2. Write a program that will compare AlphaFold's structure prediction with the true structure. So we're comparing AlphaFold's prediction for Fimbrial adhesin with the true structure for Fimbrial adhesin, then comparing AlphaFold's prediction for CST complex unit CTC1 with the true structure of CST complex unit CTC1. 
3. Get A+ 

## More details:
- We'll be using Python, because that's what we all agreed to. Plus Python has a ton of libraries developed by a bunch of smart people (we'll probably be using [numpy](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html) for eigenvalues and eigenvectors)
- Prof gave us both of the PDB structure files. Fortunate, because I'm kind of confused about how to find them on the PDB. Glad he gave them to us
- [Click here if you're wondering how to read a PDB file](https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/pdbintro.html)

## How:
1. I don't know. What is a quaternion?????????????
2. Our program needs to read the file, compute the RMSD using the algorithm given in the paper, and then output the RMSD. It sounds simple, but then again, *what is a quaternion?*

## Explanation of the algorithm
I'm doing this as best I can, because I kind of don't have any clue what I'm talking about. I hope I'm right.

### Step 1
1. xk and yk are sets of vectors. xk is the target set and yk is the model set. this means that xk is the attempt (alphafold's prediction) and yk is the truth/ideal/model upon which we judge our target (pdb true structure).
2. y with a bar over it, which i will call y bar, is given by 1/N * (the sum from y1 to yN of everything in the set yk).
3. x with a bar over it, which i will call x bar, is given by something similar, just replace all the y's with x's. 
4. x bar and y bar are the barycenters of x and y. what that means, i don't know. let's just move on. 
5. ~~we have to multiply xk and yk by the weights wk. each member of xk will have a weight, just multiply through xk by the weight that corresponds to each member of the set, i think. same with yk.~~ no weights in this program. hooray
6. ~~multiply xk and yk by weights, then~~ shift the coordinates to the barycenters (go through the set xk and subtract xbar from x1, subtract xbar from x2, ... subtract xbar from xN, now do that for yk) now we have xk squiggle and yk squiggle, sets of vectors that have been modified (standardized, maybe?) by the operations we just performed. 

### Step 2
now we use numpy to figure out the maximum eigenvalue (lambda max) and the corresponding eigenvector (cursive Q? max) of the 4x4 matrix (cursive F) given by equation 10 in the paper. equation 10 is on page 1852. i'm not writing it out here because it'd be a pain to copy over. 
to put it simply: 
1. get cursive F by solving the huge matrix equation, equation 10, found on page 1852. cursive F is a 4x4 matrix. 
2. use numpy to figure out the maximum eigenvalue and eigenvector of cursive F. this has something to do with quaternions. 
3. move on.

### Step 3
now we can obtain the best-fit RMSD. plug our values into the equation, number 3 under the algorithm section given on page 1855. 

I think that's that. 

