# =================================================================
# Input:
#     - 2d list [size, value]
#       - [[size1, value1],[size2,value2 ],.....[size10, value10]]
#     - Size of knapsack: S

# The solution to the knapsack problem is to take these items
#     [[size3, value3], [size5,value5]]
# =================================================================
# optimal substructure?
# overlapping substructure?

# EXAPMPLE TREE
    # ITEMS:
        # (weight, value)
        # (3, 4), label a
        # (2, 3), label b
        # (1, 1), label c
    # KNAPSACK
        # max_bag_cap = 5

    #                    =====(5, 0)===== 
    #                    /      |        \ 
    #                  /        |        \   
    #                a          b         c
    #             (2,4)       (3,3)     (4,1)
    #             /  \        /  \       /  \ 
    #            /   \       /   \      /   \
    #         (0,7) (1,5)  (0,7)(2,4) (1,5) (2,4)
    #          a,b   a,c   b,a   b,c   c,a   c,b
    # ==> MAXIMUM VALUE is (0,7), a->b or b->a
# =================================================================
import string

class KnapsackTreeNode:
    def __init__(self, weight: int, value: int, label: str):
        self.weight = weight
        self.value = value
        self.label = label
        self.children = dict()
           
class KnapsackTree:
    """
        This will create a tree based off items input
    """

    # create a tree based off of items
    # create a smart tree (will be unbalanced) 
        # create a datastructure that keeps track of branches. Don't bother building
        # from A -> B -> C -> D when we already have a A -> C -> B -> D 

    def __init__(self):
        self.root = KnapsackTreeNode("root")
        
    def create_tree(self, items: [[int, int]]):
        """
            Creates a tree based off input items.
            Refer to example tree. 
        """

        # create unique labels
        labels = list()
        for i in range(len(items)):
            labels.append(string[i])

        # subproblem_1: decide whether or not to take the item
        for item in items:

    
    def memoize_branches(self):
        pass
    
    def memoize_items (self):
        pass
    
    def return_max_value(self):
        pass

    
items = [[3,4],[2,3],[1,1]]
KnapsackTree(10)