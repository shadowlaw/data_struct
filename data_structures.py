
class BST:
    class Node:
        def __init__(self, value = None):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self, value=None):
        self.root = BST.Node(value)

    def search(self, value):
        if value == self.root.value:
            return self.root, 'found'
        elif value < self.root.value:
            if self.root.left is not None:
                return self.root.left.search(value)
            else:
                return self.root, 'left'
        elif value > self.root.value:
            if self.root.right is not None:
                return self.root.right.search(value)
            else:
                return self.root, 'right'

    def insert(self, value):
        if self.root.value is None:
            self.root.value = BST(value)
            return

        insertion_point = self.search(value)

        if insertion_point[1] == 'found':
            insertion_point[0].value = BST(value)
        elif insertion_point[1] == 'left':
            insertion_point[0].left = BST(value)
        elif insertion_point[1] == 'right':
            insertion_point[0].right = BST(value)

'''last test notes
    - insertion from constructor builds proper tree
    - insertion into empty tree builds deformed tree
    - refactor insertion method.
'''

bst = BST()
bst.insert(2)
bst.insert(1)
bst.insert(3)

assert bst.root.value == 2
assert bst.root.left.root.value == 1
assert bst.root.right.root.value == 3

