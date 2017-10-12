class Node:
    def __init__(self, value):
        self.value = value
        self.is_min = False


class Heap:
    def __init__(self, value=None):
        self.root = Node(value)
        self.left = None
        self.right = None

    def is_empty(self):
        return self.root.value is None

    def is_leaf(self):
        return self.root.value is not None and self.left is None and self.right is None

    def is_root(self):
        return self.root.is_min is True

    def insert(self):
        pass