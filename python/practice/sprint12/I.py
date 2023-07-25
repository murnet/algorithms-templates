class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size < self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]


def print_out(commands, size):
    queue = MyQueueSized(size)
    for cmd in commands:
        if cmd.startswith('push'):
            value = int(cmd.split()[-1])
            queue.push(value)
        elif cmd == 'peek':
            print(queue.peek())
        elif cmd == '_size':
            print(queue.size)
        elif cmd == 'pop':
            print(queue.pop())


def read_input():
    number_of_commands = int(input())
    queue_size = int(input())
    commands = [input().strip() for _ in range(number_of_commands)]
    return queue_size, commands


def main():
    size, cmds = read_input()
    print_out(cmds, size)


if __name__ == '__main__':
    main()
    # queue_cmd = [
    #     'peek',
    #     'push 5',
    #     'push 2',
    #     'peek',
    #     '_size',
    #     '_size',
    #     'push 1',
    #     '_size',
    # ]
    # queue_length = 2
    # print_out(queue_cmd, queue_length)

'''
None
5
2
2 # 5
error
2
'''
