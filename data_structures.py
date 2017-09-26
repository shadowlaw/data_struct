class Node:
    def __init__(self, value = None):
        self.value = value


class BST:
    def __init__(self, value=None):
        if value is None:
            self.root = None
            self.left = None
            self.right = None
        else:
            self.root = Node(value)
            self.left = None
            self.right = None

    def search(self, value):
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
        if self.root is None:
            self.root = Node(value)
            return

        node, status= self.search(value)

        if status == "found":
            node.value = value
        elif status == 'right':
            node.right = BST(value)
        elif status == 'left':
            node.left = BST(value)


bst = BST()
bst.insert(2)
bst.insert(3)
bst.insert(1)
bst.insert(9)
bst.insert(4)
bst.insert(-1)

