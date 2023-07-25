# ID посылки -
class DequeIsFullError(Exception):
    """Exception raised if deque is full."""
    def __init__(self, message='Deque is full'):
        self.message = message
        super().__init__(self.message)


class DequeIsEmptyError(Exception):
    """Exception raised if deque is empty."""
    def __init__(self, message='Deque is empty'):
        self.message = message
        super().__init__(self.message)


class Deque:
    def __init__(self, limit):
        self._items = [None] * limit
        self._limit = limit
        self._head = 0
        self._tail = 0
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._limit

    def push_back(self, value):
        if self.is_full():
            raise DequeIsFullError
        self._items[self._tail] = value
        self._tail = (self._tail + 1) % self._limit
        self._size += 1

    def push_front(self, value):
        if self.is_full():
            raise DequeIsFullError
        self._head = (self._head - 1) % self._limit
        self._items[self._head] = value
        self._size += 1

    def pop_front(self):
        if self.is_empty():
            raise DequeIsEmptyError
        value = self._items[self._head]
        self._head = (self._head + 1) % self._limit
        self._size -= 1
        return value

    def pop_back(self):
        if self.is_empty():
            raise DequeIsEmptyError
        self._tail = (self._tail - 1) % self._limit
        value = self._items[self._tail]
        self._items[self._tail] = None
        self._size -= 1
        return value


def read_input():
    number_of_commands = int(input())
    deque_max_size = int(input())
    commands = [input().strip() for _ in range(number_of_commands)]
    return deque_max_size, commands


def print_out(size, commands):
    dek = Deque(size)
    commands_dict = {
        'push_front': dek.push_front,
        'push_back': dek.push_back,
        'pop_front': dek.pop_front,
        'pop_back': dek.pop_back,
    }
    for cmd in commands:
        if cmd.startswith('push'):
            command, value = cmd.split()
            try:
                commands_dict[command](value)
            except (DequeIsEmptyError, DequeIsFullError):
                print('error')
        else:
            try:
                print(commands_dict[cmd]())
            except (DequeIsEmptyError, DequeIsFullError):
                print('error')


if __name__ == '__main__':
    deque_size, cmds = read_input()
    print_out(deque_size, cmds)
