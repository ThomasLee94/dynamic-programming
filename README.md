# Dynamic Programming

## The Knapsack Problem

from [wikipedia](https://en.wikipedia.org/wiki/Knapsack_problem) it is defined as follows:

    “given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.”

In other words:
    - Knapsack has a MAX_CAPACITY. 
    - Items have a WEIGHT and VALUE.
    - What is the most amount of VALUE we can get in a given knapsack of MAX_CAPACITY? 

### The 5 steps

1 - Identify the sub-problems
2 - Guess first choice
3 - Recursively define the value of an optimal solution
4 - Compute the value of an optimal solution
5 - Solve original problem - reconstruct from sub-problems

