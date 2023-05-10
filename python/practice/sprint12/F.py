class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            self.items.pop()
            return
        print('error')

    def get_max(self):
        if self.items:
            return max(self.items)
        return None


def print_out(data):
    stack = StackMax()
    for cmd in data:
        if 'get' in cmd:
            print(stack.get_max())
        if cmd == 'pop':
            stack.pop()
        if 'push' in cmd:
            num = int(cmd.split()[-1])
            stack.push(num)


def read_input():
    number_of_commands = int(input())
    arr = [input().strip() for _ in range(number_of_commands)]
    return number_of_commands, arr


def main():
    num, cmds = read_input()
    print_out(cmds)


if __name__ == '__main__':
    main()

# commands = ['get_max', 'pop', 'pop', 'pop', 'push 10', 'get_max', 'push -9']
# print_out(commands)
#
# cmds = ['get_max', 'push 7', 'pop', 'push -2', 'push -1', 'pop', 'get_max', 'get_max']
# print_out(cmds)
