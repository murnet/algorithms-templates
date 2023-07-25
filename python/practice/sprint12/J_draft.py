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

        if self.q_size == 1:
            x = self.head
            self.head = self.tail = None
            self.q_size -= 1
            return x.value
        if self.q_size == 2:
            x = self.head
            self.head = self.tail
            self.q_size -= 1
            return x.value
        else:
            x = self.head
            self.head = self.head.next_item
            self.q_size -= 1
            return x.value

    def put(self, x):
        if self.q_size == 0:
            self.head = Node(value=x)
            self.tail = self.head
        else:
            self.head.next_item = Node(value=x)
            # self._tail.next_item.next_item = self._head
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
        elif cmd == '_size':
            print(queue.size())


def read_input():
    number_of_commands = int(input())
    commands = [input().strip() for _ in range(number_of_commands)]
    return commands


def get_data(data):
    cmds = []
    for line in data.strip().splitlines():
        if line.isdecimal():
            pass
        else:
            cmds.append(line.strip())
    return cmds


def main():
    # print_out(read_input())
    data = '''
    10
    put -34
    put -23
    get
    _size
    get
    _size
    get
    get
    put 80
    _size
    '''
    print_out(get_data(data))
    # print(get_data(data))


if __name__ == '__main__':
    main()
