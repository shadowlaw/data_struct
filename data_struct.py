"""Implements data basic structures

Data Structures implemented:
- Binary Search Tress (BST - Node class required for use.)
- Red Black Trees (RBT - Node class requited for use.)
- Binary Heaps (BH - Node class required for use)
- Stacks
"""


class Node:
    """Node class, holds a value for the BST data structure."""

    def __init__(self, value=None):
        """Initializes value attribute for node

        :param
        value - initialized to none. Assigned instance variable to the hold node value.
        """
        self.value = value
        self.parent = None
        self.name = None


class BST:
    """Binary search Tree class. Implements a simple binary search tree."""

    def __init__(self, value=None):
        """Constructor for BST.

        :param
        value - initialized to none. Added to the  BST root node.
        """
        if value is None:
            self.root = None
            self.left = None
            self.right = None
        else:
            self.root = Node(value)
            self.left = None
            self.right = None

    def is_empty(self):
        """Returns True if the tree is empty, false otherwise."""

        return self.root is None and self.left is None and self.right is None

    def is_leaf(self):
        """Returns true if node is a leaf, false otherwise"""

        return self.left is None and self.right is None

    def search(self, value):
        """Locates the passed value.

        :param
        value - value to be located.

        :returns
        tuple containing node and node location for value to be placed.
        """

        if self.is_empty():
            return Node(), 'Empty tree'

        if value == self.root.value:
            return self, "found"

        if value > self.root.value:
            if self.right is not None:
                return self.right.search(value)
            else:
                return self, 'right'

        if value < self.root.value:
            if self.left is not None:
                return self.left.search(value)
            else:
                return self, 'left'

    def insert(self, value):
        """Inserts a value into the BST using the search method.

        :param
        value - value to be inserted

        """

        if self.is_empty():
            self.root = Node(value)
            self.root.name = 'root'
            return

        node, status = self.search(value)

        if status == "found":
            node.root.value = value
        elif status == 'right':
            node.right = BST(value)
            node.right.root.parent = node
            node.right.root.name = "right"
        elif status == 'left':
            node.left = BST(value)
            node.left.root.parent = node
            node.left.root.name = "left"

    def successor(self):
        """Locates tree successor for node passed.

        :return
        returns successor for node passed, false otherwise.
        """
        pass

    def delete_node(self, value):
        """Locates node to be removed.

        :param
        value - value of the node to be removed

        :return
        returns true on successful deletion, false if node is not found.
        """

        def remove_node(to_remove):
            """Removes node from bst parent node instance.

            :param
            to_remove - node to be removed.
            """
            if to_remove.root.name == "left":
                node.root.parent.left = None
            else:
                node.root.parent.right = None

        node, status = self.search(value)

        if status != 'found':
            return False

        if node.is_leaf():
            remove_node(node)
            return True

        if node.right is not None:
            pass
            # find node successor
            # replace node with successor



bst = BST()
bst.insert(2)
bst.insert(3)
bst.insert(1)
bst.insert(0)
bst.insert(4)

print(bst.delete_node(4))
print("Finished")
