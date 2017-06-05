class Queue:
    def __init__(self, size):
        self.i = 0
        self.queue = ['' for _ in range(size)]

    def put(self, item):
        self.queue[self.i] = item
        self.i += 1

    def get(self):
        self.i -= 1
        return self.queue[self.i]

    def size(self):
        return self.i

    def empty(self):
        return self.i == 0

    def clean(self):
        self.i = 0

    def peek(self):
        return self.queue[self.i - 1]