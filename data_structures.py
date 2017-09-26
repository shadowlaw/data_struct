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

    def search(self, value):
        '''Locates the passed value.

        :param
        value - value to be located.

        :returns
        tuple containing node and node location for value to be placed.
        '''

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
        '''inserts a value into the BST using the search method.

        :param
        value - value to be inserted
        
        '''
        if self.root is None:
            self.root = Node(value)
            return

        node, status = self.search(value)

        if status == "found":
            node.value = value
        elif status == 'right':
            node.right = BST(value)
        elif status == 'left':
            node.left = BST(value)
