class myStack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        
        if not self.stack:
            return None
        
        return self.stack.pop()

    def size(self):
        return len(self.stack)
