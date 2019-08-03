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
           
class KnapsackTree:
    """
        This will create a tree based off items input
    """

    # create a tree based off of items
    # create a smart tree (will be unbalanced) 
        # create a datastructure that keeps track of branches. Don't bother building
        # from A -> B -> C -> D when we already have a A -> C -> B -> D 

    def __init__(self, max_bag_cap: int, value=0, label="start"):
        self.weight = max_bag_cap
        self.value = 0
        self.label = label
    
    def create_tree(self, items: [[int, int]]):
        """
            Creates a tree based off input items.
            Refer to example tree. 
        """

        # subproblem_1: decide whether or not to take the item
        pass
    
    def memoize(self):
        pass
    
    def return_max_value(self):
        pass

    
items = [[3,4],[2,3],[1,1]]