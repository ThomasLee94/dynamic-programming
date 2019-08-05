# =================================================================
# Input:
#     - 2d list [size, value]
#       - [[size1, value1],[size2,value2 ],.....[size10, value10]]
#     - Size of knapsack: S

# The solution to the knapsack problem is to take these items
#     [[size3, value3], [size5,value5]]
# =================================================================

from classes.tree import KnapsackTree

def __main__():
    items = [[3,4],[2,3],[1,1]]
    empty_tree = KnapsackTree(10)
    tree = empty_tree.insert_all_items(items)
    max_value = tree.return_max_value
    return max_value

main()