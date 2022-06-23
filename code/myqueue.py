class myQueue:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, element):
        self.queue.insert(0, element)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)



