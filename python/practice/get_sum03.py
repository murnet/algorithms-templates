def get_sum(a, b):
    result = a + b
    return str(result)


def read_input():
    data = input()
    a, b = data.split()
    return int(a), int(b)


a, b = read_input()
print(get_sum(a, b))
