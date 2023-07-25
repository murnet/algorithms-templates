# ID посылки - 89260233
class StackIsEmptyError(Exception):
    """Exception raised if stack is empty."""

    def __init__(self, message='Stack is empty'):
        self.message = message
        super().__init__(self.message)


class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self.is_empty():
            return self._items.pop()
        raise StackIsEmptyError


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
        elif item in '+-*/':
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operators[item](operand1, operand2)
            stack.push(result)
        else:
            raise Exception('something went wrong(:')

    return stack.pop()


if __name__ == '__main__':
    data_string = input()
    print(calculator(data_string))
