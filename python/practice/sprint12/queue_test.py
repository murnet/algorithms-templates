class Queue:
    def __init__(self):
        self.items = []

    def push_back(self, item):
        self.items.append(item)

    def push_front(self, item):
        self.items.insert(0, item)

    def pop_back(self):
        self.items.pop()

    def pop_front(self):
        self.items.pop(0)