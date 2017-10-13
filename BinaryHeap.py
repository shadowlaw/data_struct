class Node:
    def __init__(self, value):
        self.value = value
        self.is_min = True
        self.left = None
        self.right = None


class Heap:
    class Queue:
        def __init__(self):
            self.__queue = []

        def empty(self):
            return self.__queue == []

        def put(self, value):
            self.__queue.append(value)

        def get(self):
            if not self.empty():
                return self.__queue.pop(0)

            return False

        def __contains__(self, item):
            return item in self.__queue

    def __init__(self, value=None):
        self.root = Node(value)
        self.__add_to = 'left'
        self.__node_add_to = self.root
        self.__level_queue = Heap.Queue()

    def is_empty_heap(self):
        return self.root.value is None

    def is_leaf(self):
        return self.root.value is not None and self.root.left is None and self.root.right is None

    def is_root(self):
        return self.root.is_min is True

    def insert(self, value):
        def add_to_queue(node):
            if node.left is not None and node.left not in self.__level_queue:
                self.__level_queue.put(node.left)
            if node.right is not None and node.right not in self.__level_queue:
                self.__level_queue.put(node.right)

        if self.is_empty_heap():
            self.root.value = value
            return True

        if self.__add_to == 'left':
            self.__node_add_to.left = Node(value)
            self.__node_add_to.left.is_min = False
            self.__add_to = "right"
            add_to_queue(self.__node_add_to)
            return True

        elif self.__add_to == 'right':
            self.__node_add_to.right = Node(value)
            self.__node_add_to.right.is_min = False
            self.__add_to = "left"
            add_to_queue(self.__node_add_to)

            if not self.__level_queue.empty():
                self.__node_add_to = self.__level_queue.get()

            return True


h = Heap()
h.insert(2)
h.insert(8)
h.insert(9)
h.insert(10)
print("")