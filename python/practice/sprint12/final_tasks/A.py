
class Deq:
    def __init__(self, limit):
        self.items = [None] * limit
        self.limit = limit
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, value):
        if self.size != self.limit:
            self.items[self.tail] = value
            self.tail = (self.tail + 1) % self.limit
            self.size += 1
        else:
            return 'error'

    def push_front(self, value):
        if self.size != self.limit:
            self.items[self.head - 1] = value
            self.head = (self.head - 1) % self.limit
            self.size += 1
        else:
            return 'error'

    def pop_front(self):
        if self.is_empty():
            return 'error'
        value = self.items[self.head]
        self.head = (self.head + 1) % self.limit
        self.size -= 1
        return value

    def pop_back(self):
        if self.is_empty():
            return 'error'
        value = self.items[self.tail - 1]
        self.items[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.limit
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
            print(commands_dict[command](value))
        else:
            print(commands_dict[cmd])


if __name__ == '__main__':
    data_1 = '''4
4
push_front 861
push_front -819
pop_back
pop_back
'''
    num, cmd = parse_data(data_1)
    print_out(num, cmd)