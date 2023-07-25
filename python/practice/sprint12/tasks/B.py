# ID посылки - 89257283
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError('error')

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None


def is_operator(items):
    return items in '+-*/'


operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
}


def calculator(data):
    stack = Stack()
    data = data.split()

    for item in data:
        if item.isdigit() or (item.startswith('-') and item[1:].isdigit()):
            stack.push(int(item))
        elif is_operator(item):
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operators[item](operand1, operand2)
            stack.push(result)
        else:
            raise Exception('something went wrong(:')

    return stack.peek()


def read_input():
    data_string = input()
    return data_string


if __name__ == '__main__':
    data_input = read_input()
    print(calculator(data_input))
