class Node:
    def __init__(self, value = None):
        self.value = value


class BST:
    def __init__(self, value=None):
        self.root = Node(value)
        self.left = None
        self.right = None

    def search(self, value):
        if value == self.root.value:
            return self.root, "found"

        if self.right is not None:
            if value > self.root.value:
                return self.right.search(value)
        else:
            return self, 'right'

        if self.left is not None:
            if value < self.root.value:
                return self.left.search(value)
        else:
            return self, 'left'

bst = BST(2)
bst.right = BST(3)
bst.left = BST(1)
bst.right.right = BST(9)
bst.right.left = BST(4)

print(bst.search(9)[0].value)

assert bst.root.value == 2
assert bst.left.root.value == 1
assert bst.right.root.value == 3
assert bst.right.right.root.value == 9
assert bst.right.left.root.value == 4
