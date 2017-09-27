'''Implements data basic structures

Data Structures implemented:
- Binary Search Tress (BST - Node class required for use.)
- Red Black Trees (RBT - Node class requited for use.)
=[
'''
class Node:
    '''Node class, holds a value for the BST data structure.'''

    def __init__(self, value = None):
        '''Initializes value attribute for node

        :param
        value - initialized to none. Assigned instance variable to the hold node value.
        '''
        self.value = value


class BST:
    '''Binary search Tree class. Implements a simple binary search tree.'''

    def __init__(self, value=None):
        '''Constructor for BST.

        :param
        value - initialized to none. Added to the  BST root node.
        '''
        if value is None:
            self.root = None
            self.left = None
            self.right = None
        else:
            self.root = Node(value)
            self.left = None
            self.right = None

    def is_empty(self):
        '''Returns True if the tree is empty, false otherwise.'''

        return self.root == None and self.left == None and self.right == None

    def is_leaf(self):
        '''Returns true if node is a leaf, false otherwise'''

        return self.left == None and self.right == None

    def search(self, value):
        '''Locates the passed value.

        :param
        value - value to be located.

        :returns
        tuple containing node and node location for value to be placed.
        '''

        if self.is_empty():
            return Node(), 'Empty tree'

        if value == self.root.value:
            return self.root, "found"

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
        '''Inserts a value into the BST using the search method.

        :param
        value - value to be inserted

        '''

        if self.is_empty():
            self.root = Node(value)
            return

        node, status = self.search(value)

        if status == "found":
            node.value = value
        elif status == 'right':
            node.right = BST(value)
        elif status == 'left':
            node.left = BST(value)

    def successor(self, node):
        '''Locates tree successor for node passed.

        :param
        node - node for which to find successor.

        :return
        returns successor for node passed, false otherwise.
        '''
        pass


    def delete_node(self, value):
        '''Locates node to be removed.

        :param
        value - value of the node to be removed

        :return
        returns true on successful deletion, false if node is not found.
        '''

        def remove_node(parent_node, indicator):
            '''Removes node from bst parent node instance.

            :param
            parent_node - parent node of node to be removed.
            indicator - indicates either left or right node to be removed from parent node.
            '''
            pass
