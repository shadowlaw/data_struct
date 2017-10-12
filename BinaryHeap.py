class Node:
    def __init__(self, value):
        self.value = value
        self.is_min = False


class Heap:
    def __init__(self, value=None):
        if value is None:
            self.root = None
            self.left = None
            self.right = None
        else:
            self.root = Node(value)
            self.left = None
            self.right = None

