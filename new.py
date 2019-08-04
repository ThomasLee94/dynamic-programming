 def is_parent_node(self, label):
        """
            Returns a boolean
        """

        # Start with the root node and keep track of its parent
        node = self.root

        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if node.label == label:
                # Return the parent of the found node
                return True
            # Check if the given item is less than the node's data
            elif node.label < label:
                # Update the parent and descend to the node's left child
                parent = node
                node = node.children[label]
            # Check if the given item is greater than the node's data
            elif node.label > label:
                # Update the parent and descend to the node's right child
                parent = node
                node = node.children[label]
        # Not found
        return False