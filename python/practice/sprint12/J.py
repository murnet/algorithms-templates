class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.q_size = 0

    def _is_empty(self):
        return self.q_size == 0

    def get(self):
        if self._is_empty():
            return 'error'

        head_value = self.head.value
        self.head = self.head.next_item
        self.q_size -= 1

        if self.q_size == 0:
            self.tail = None

        return head_value

    def put(self, value):
        new_node = Node(value)
        if self._is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next_item = new_node
            self.tail = new_node
        self.q_size += 1

    def size(self):
        return self.q_size


def print_out(commands):
    queue = Queue()
    for cmd in commands:
        if cmd.startswith('put'):
            value = int(cmd.split()[-1])
            queue.put(value)
        elif cmd == 'get':
            print(queue.get())
        elif cmd == 'size':
            print(queue.size())


def read_input():
    number_of_commands = int(input())
    commands = [input().strip() for _ in range(number_of_commands)]
    return commands


def main():
    commands = read_input()
    print_out(commands)


if __name__ == '__main__':
    main()
