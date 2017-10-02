class Stack:
    """First In First Out (FIFO) data structure"""

    def __init__(self):
        self.__holder = []

    def is_empty(self):
        return self.__holder == []

    def stack(self):
        return self.__holder

    def push(self, element):
        self.__holder.append(element)
        return True

    def pop(self):
        if not self.is_empty():
            return self.__holder.pop()
        else:
            return False

    def print_stack(self):
        if self.is_empty():
            return "Stack is Empty."
        string = ""
        for x in range(len(self.__holder)):
            string += " {0}".format(self.__holder[x])

        print(string+" <- Top")
