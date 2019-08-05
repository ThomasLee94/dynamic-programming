class KnapsackTreeNode:
    def __init__(self, label: str, weight: int, value=0):
        self.weight = weight
        self.value = value
        self.label = label
        self.children = dict()

        # EXAMPLE CHILDREN DICT
            #  {
                # "root": KnapsackTreeNode(LABEL, max_bag_cap - ITEM_WEIGHT, item_value + ITEM_VALUE)
            # }
    
    def is_leaf(self):
        """
            Returns true if node has no children.
        """

        return self.children is None
           