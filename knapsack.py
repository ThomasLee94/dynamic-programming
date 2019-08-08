# =================================================================
# Input:
#     - 2d list [size, value]
#       - [[size1, value1],[size2,value2 ],.....[size10, value10]]
#     - Size of knapsack: S

# The solution to the knapsack problem is to take these items
#     [[size3, value3], [size5,value5]]
# =================================================================

# from classes.tree import KnapsackTree


# def knapsack_bad():
#     items = [[3, 4], [2, 3], [1, 1]]
#     empty_tree = KnapsackTree(10)
#     tree = empty_tree.insert_all_items(items)
#     node_weight, highest_value, visited_list = tree.return_max_value
#     return highest_value


# knapsack_bad()


def knapsack(
    bag_cap: int, items: [[str, int, int]], mem_val_index: dict, item_index=0
) -> int:
    """
        This functions returns the highest value of combined given items
        to the constraint of the knapsack capacity. 
    """
    # MEMOIZED DICT EXAMPLE
    # {
    #   (capacity, item_index): total_value
    # }

    # if values are already memoized, retrieve from dict
    if (bag_cap, item_index) in mem_val_index:
        return mem_val_index[(bag_cap, item_index)]

    else:
        # === BASE CASES ===
        # case: item index exceeds length of items list
        if item_index >= len(items):
            return 0
        # case: no items
        if len(items) == 0:
            return 0
        # case: knapsack capacity exceeded
        if bag_cap <= 0:
            return 0

        item = items[item_index]
        item_weight = item[1]
        item_value = item[2]

        if item[1] > bag_cap:
            return knapsack(bag_cap, items, mem_val_index, item_index + 1)

        # === DECISION TREE ===
        # we add item_value because it doesn't have the item_value from the
        # previous recursive call
        # add current item
        item_add = (
            knapsack(
                bag_cap - item_weight, items, mem_val_index, item_index + 1
            )
            + item_value
        )
        # no need to add item_value from the previous recurisve call
        # dont' add current item
        item_not_add = knapsack(
            bag_cap, items, mem_val_index, item_index + 1
        )

        # get the maximum from both decisions from tree
        total_value = max(item_add, item_not_add)
        # update memoization 
        mem_val_index[(bag_cap, item_index)] = total_value

        return total_value


print(knapsack(10, [["a", 2, 3], ["b", 3, 1], ["d", 8, 1]], {}))
