from classes.node import KnapsackTreeNode
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
#           ^           X           X     X
#          a,b   a,c   b,a   b,c   c,a   c,b
# ==> MAXIMUM VALUE is (0,7), a->b or b->a
# =================================================================


class KnapsackTree:
    """
        This will create a tree based off items input. 
    """

    def __init__(self, max_bag_cap: int):
        """
            Initialises tree with max knapsack capacity. 
        """
        self.root = KnapsackTreeNode("root", max_bag_cap)

    def create_labels(self, items) -> set:
        """
            Creates unique labels for items to be evaluated for memoization.
        """

        labels_set = set()
        labels_list = list()
        for i in range(len(items)):
            labels_set.add(string.ascii_letters[i])
            labels_list.append(string.ascii_letters[i])

        return labels_set, labels_list

    def insert_all_items(
        self,
        items: [[int, int]],
        memoized_branches=None,
        items_label_set=None,
        parent_node=None,
        node=None,
    ) -> object:
        """
            Creates tree recursively based on items per level.
            Refer to example tree structure.
        """

        # start nodes
        if node is None:
            node = self.root

        # labels set
        if items_label_set is None:
            items_label_set, labels_list = self.create_labels(items)

        # recursion vars
        parent = None
        child = None

        # Recursively create tree
        for i in range(len(items)):
            if KnapsackTree is None:
                # init vars
                item_label = labels_list[i]
                item_weight = items[i][0]
                item_value = items[i][1]
                # start of recursion, no parent
                if parent_node is None:
                    # check if label exists in children dict
                    if not node.children[labels_list[i]]:
                        # check if max weight has been reached
                        if (node.weight - item_weight) >= 0:
                            # CONDITION TO CHECK IF ITEM LABEL IS NOT IN
                            # A PATH IN ANOTHER BRANCH ON A HIGHER LEVEL
                            if memoized_branches is not None:
                                # loop through inner 2d list of memoized branches
                                for branch in memoized_branches:
                                    if item_label != branch[-1]:
                                        # IF ITEM NOT IN ANY OTHER BRANCH ON A +1 LEVEL
                                        if not parent.childred[item_label]:
                                            # add key-value pairs
                                            item_label = KnapsackTreeNode(
                                                item_label,
                                                node.weight - item_weight,
                                                node.value + item_value,
                                            )
                        else:
                            # if max weight has been exceeded
                            return

                else:
                    # vars for memoization
                    parent_label = parent.label
                    child_label = child.label
                    # memoize branch labels
                    memoized_branches = self.memoize_branches(
                        parent_label, child_label
                    )

                # keeping track of parent and children to check
                # other branches when creating new ones.
                parent = node
                child = node.children[item_label]

        # 1st recursive call onwards
        return self.insert_all_items(
            items, memoized_branches, items_label_set, parent, child
        )

    def memoize_branches(self, parent_label, child_label, branches=None):
        """
            Creates a 2d list of memoized labels of branches.
        """
        # EXAMPLE MEMOIZATION OF BRANCHES
        # [
        #   ["root", "a", "b", ...],
        #   ["root", "a", "c", ...],
        #   ["root", "b", "a", ...],
        #   ["root", "b", "c", ...],
        #   ["root", "c", "a", ...],
        #   ["root", "c", "b", ...],
        # ]

        if branches is None:
            branches = list()

        for branch in branches:
            if len(branches) == 0:
                branches.append([parent_label, child_label])
            else:
                if branch[-1] == parent_label:
                    branch.append(child_label)

        return branches

    def return_max_value(
        self, visited_list: [str], visited_set, node=None, highest_value=0
    ) -> (int, int, [str]):
        """
                Returns the max value of the constructed tree with
                remaining bag weight and visited nodes.
                Args
                    visited_list: keeps track of visited verticies in order of
                    traversal.
                    visited: set method to keep track of visited verticies.
                Returns
                    remaining_weight, highest_value, visited_nodes: [str]
            """

        node = self.root

        if node not in visited_set:
            # Add vertex_a to set
            visited_set.add(node.label)
            # add vertex to visited list in order
            visited_list.append(node.label)
            # if vertex_b is found
            if node.value > highest_value:
                highest_value = node.value
            # add neighbours of vertex_a in stack
            for child in node.children:
                # visit neighbours recursively
                return self.return_max_value(child, visited_list, visited_set)

        # Catch all
        return node.weight, highest_value, visited_list
