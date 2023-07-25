# ID посылки - 89256461
class Deque:
    def __init__(self, limit):
        self.items = [None] * limit
        self.limit = limit
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.limit

    def push_back(self, value):
        if self.is_full():
            raise Exception('error')
        self.items[self.tail] = value
        self.tail = (self.tail + 1) % self.limit
        self.size += 1

    def push_front(self, value):
        if self.is_full():
            raise Exception('error')
        self.head = (self.head - 1) % self.limit
        self.items[self.head] = value
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise Exception('error')
        value = self.items[self.head]
        self.head = (self.head + 1) % self.limit
        self.size -= 1
        return value

    def pop_back(self):
        if self.is_empty():
            raise Exception('error')
        self.tail = (self.tail - 1) % self.limit
        value = self.items[self.tail]
        self.items[self.tail] = None
        self.size -= 1
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
            except Exception as error:
                print(error)
        else:
            try:
                print(commands_dict[cmd]())
            except Exception as error:
                print(error)


if __name__ == '__main__':
    deque_size, cmds = read_input()
    print_out(deque_size, cmds)
