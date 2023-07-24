class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.q_size = 0

    def is_empty(self):
        return self.q_size == 0

    def get(self):
        if self.is_empty():
            return 'error'

        front_value = self.front.value
        self.front = self.front.next_node
        self.q_size -= 1

        if self.q_size == 0:
            self.rear = None

        return front_value

    def put(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next_node = new_node
            self.rear = new_node

        self.q_size += 1

    @property
    def size(self):
        return self.q_size


def read_input():
    number_of_commands = int(input())
    commands = [input().strip() for _ in range(number_of_commands)]
    return commands


def process_commands(commands):
    queue = Queue()
    for cmd in commands:
        if cmd.startswith('put'):
            value = int(cmd.split()[-1])
            queue.put(value)
        elif cmd == 'get':
            print(queue.get())
        elif cmd == 'size':
            print(queue.size)


def main():
    commands = read_input()
    process_commands(commands)


if __name__ == '__main__':
    main()
