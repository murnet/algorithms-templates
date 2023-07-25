# ID посылки - 89259718
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


def print_out(size, commands):
    deque = Deque(size)
    for cmd in commands:
        if cmd.startswith('push'):
            command, value = cmd.split()
            try:
                getattr(deque, command)(value)
            except (DequeIsEmptyError, DequeIsFullError):
                print('error')
        else:
            try:
                print(getattr(deque, cmd)())
            except (DequeIsEmptyError, DequeIsFullError):
                print('error')


if __name__ == '__main__':
    number_of_commands = int(input())
    deque_max_size = int(input())
    commands_list = [input().strip() for _ in range(number_of_commands)]
    print_out(deque_max_size, commands_list)
