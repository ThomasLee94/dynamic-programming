# The Egg Dropping puzzle

Suppose that we wish to know which stories in a 36-story building are safe to drop eggs from, and which will cause the eggs to break on landing.

Assumptions:
    - An egg that survives a fall can be used again.
    - A broken egg must be discarded.
    - The effect of a fall is the same for all eggs.
    - If an egg breaks when dropped, then it would break if dropped from a higher floor.
    - If an egg survives a fall then it would survive a shorter fall.
    - It is not ruled out that the first-floor windows break eggs, nor is it ruled out that the 36th floor do not cause an egg to break.

Suppose 2 eggs are available, what is the minimum number of drops required to know from which if egg the egg is dropped, it will break. 

We are minimising the use of eggs to find the pivotal floor in the worst case. 

## The 5 Steps to DP
    - 1 Identify the sub-problems
        a. Where do we make the first egg drop? How do we figure out the rest after the first drop.
        b. Whether the egg breaks or not. 
    - 2 Guess first choice
        a. Where we make the first egg drop. 
    - 3 Recursively define the value of an optimal solution
        a. Computing whether egg breaks or not for every floor bottom up.
    - 4 Compute the value of an optimal solution
        a. Getting the maximum value of egg & broken_egg
        b. We minimising the number of drops needed to find the pivotal floor in which the egg drops. 
    - 5 Solve original problem - reconstruct from sub-problems
        a. Solution is the max. 
