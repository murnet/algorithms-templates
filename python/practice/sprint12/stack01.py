class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False


if __name__ == '__name__':
    stack = Stack()
    stack.push('apple')
    stack.push('banana')
    stack.push('orange')
