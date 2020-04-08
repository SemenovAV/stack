class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return not bool(self.stack)

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[self.size() - 1]

    def size(self):
        return len(self.stack)
