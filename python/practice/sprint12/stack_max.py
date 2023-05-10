class StackMax:
    def __init__(self):
        self.items = []
        self.max_stack = []

    def push(self, item):
        self.items.append(item)
        if not self.max_stack or item >= self.max_stack[-1]:
            self.max_stack.append(item)

    def pop(self):
        if self.items:
            item = self.items.pop()
            if item == self.max_stack[-1]:
                self.max_stack.pop()
        else:
            raise IndexError("Cannot pop from an empty stack.")

    def get_max(self):
        if self.max_stack:
            return self.max_stack[-1]
        return None


def print_out(data):
    stack = StackMax()
    command_map = {
        'get_max': stack.get_max,
        'pop': stack.pop,
        'push': lambda x: stack.push(int(x.split()[-1])),
    }
    for cmd in data:
        if cmd in command_map:
            result = command_map[cmd]()
            if result is not None:
                print(result)


commands = ['get_max', 'pop', 'pop', 'pop', 'push -9']
