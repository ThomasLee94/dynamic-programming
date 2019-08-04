 def is_not_parent_parent_node(self, label, node):
        """
            Returns a boolean
        """

        # Start with the root node and keep track of its parent
        node = self.root

        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if labels match
            if node.label == label:
                # Return true
                return True
            # else, traverse through tree
            else:
                parent = node
                node = node.children[label]
        # Not found
        return False