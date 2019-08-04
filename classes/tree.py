from node import KnapsackTreeNode
import string

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

    def __init__(self, max_bag_cap: int):
        self.root = KnapsackTreeNode("root", max_bag_cap)
    
    def create_labels(self, items)->set:
        # create unique labels for all items
        labels_set = set()
        labels_list = list()
        for i in range(len(items)):
            labels_set.add(string.ascii_letters[i])
            labels_list.append(string.ascii_letters[i])
        
        return labels_set, labels_list
        
    def insert_all_items(self, items: [[int, int]], items_label_set=None, node=None) -> object:
        """
            Creates tree based on items.
            Refer to example tree. 
        """
        # create a smart tree (will be unbalanced) 
        # create a datastructure that keeps track of branches. Don't bother building
        # from A -> B -> C -> D when we already have a A -> C -> B -> D 
        
        # start nodes
        if node is None:
            node = self.root
        
        # labels set
        if items_label_set is None:
            items_label_set, labels_list = self.create_labels(items)
        
        # Recursively create tree
        for i in range(items):
            if KnapsackTree is None:
                item_label = labels_list[i]
                item_weight = items[i][0]
                item_value = items[i][1]
                # check if label exists in children dict
                if not node.children[labels_list[i]]:
                    # check if max weight has been reached
                    if (node.weight - item_weight) <= 0:
                        
                        # update values accordingly
                        item_label = KnapsackTreeNode(item_label, node.weight - item_weight, node.value + item_value)
                # if it does, traverse through tree
                node = node.children[item_label]

        # subproblem_1: decide whether or not to take the item
        return self.insert_all_items(items, items_label_set, node)
    
    def memoize_branches(self)->[(int)]:
        pass

        # if path exists, don't create

    
    def memoize_items(self, items: [[int, int]]):
        pass

    def return_max_value(self):
        """
            Returns the max value of the constructed tree 
        """
        node = self.root