class Deq:
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


def parse_data(data):
    nums = []
    commands = []
    for line in data.strip().splitlines():
        if line.isdecimal():
            nums.append(int(line.strip()))
        else:
            commands.append(line.strip())
    return nums, commands


def print_out(nums, commands):
    dek = Deq(nums[-1])
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
            except Exception as e:
                print(str(e))
        else:
            try:
                print(commands_dict[cmd]())
            except Exception as e:
                print(str(e))


if __name__ == '__main__':
    data_1 = '''4
4
push_front 861
push_front -819
pop_back
pop_back
'''
    data_2 = '''7
10
push_front -855
push_front 0
pop_back
pop_back
push_back 844
pop_back
push_back 823
'''
    data_3 = '''6
6
push_front -201
push_back 959
push_back 102
push_front 20
pop_front
pop_back
'''
    num, cmds = parse_data(data_2)
    print_out(num, cmds)
