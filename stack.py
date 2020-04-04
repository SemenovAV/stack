class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return not bool(self.stack)

    def push(self, element):
        self.stack.insert(0, element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.stack[0]

    def size(self):
        return len(self.stack)
