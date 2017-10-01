"""Implements Binary search tree data structure (Node class needed for implementation)."""


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

    def is_root(self):
        return True if self.root.name == "root" else False

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
        if self.right is None:
            return False

        if self.right.left is None:
            return self.right

        temp_node = self.right.left

        while temp_node.left is not None:
            temp_node = temp_node.left

        return temp_node

    def delete_node(self, value):
        """Locates node to be removed.

        :param
        value - value of the node to be removed

        :return
        returns True on successful node removal, False if node is not found.
        """

        def remove_node(to_remove):
            """Removes node from bst parent node instance.

            :param
            to_remove - node to be removed.
            """
            if to_remove.root.name == "left":
                to_remove.root.parent.left = None
            else:
                to_remove.root.parent.right = None

        node, status = self.search(value)

        if status != 'found':
            return False

        if node.is_root():
            if node.is_leaf():
                node.root = BST()
                return True

            if node.right is not None:
                successor = node.successor()
                node.root.value = successor.root.value

                if successor.right is not None:
                    if successor.root.name == 'left':
                        successor.root.parent.left = successor.right
                    else:
                        successor.root.parent.right = successor.right

                    successor.root.parent = None

                if successor.is_leaf():
                    remove_node(successor)

                return True
            else:
                node.root.value = node.left.root.value
                node.left = node.left.left

                if node.left is not None:
                    node.left.root.parent = node

                return True

        if node.is_leaf():
            remove_node(node)
            return True

        if node.right is not None:
            successor = node.successor()
            node.root.value = successor.root.value

            if successor.right is not None:
                if successor.root.name == 'left':
                    successor.root.parent.left = successor.right
                else:
                    successor.root.parent.right = successor.right

                successor.root.parent = None

            if successor.is_leaf():
                remove_node(successor)

            return True
        elif node.left is not None:
            node.left.root.parent = node.root.parent
            node.root.parent.left = node.left
            return True

