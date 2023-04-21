# ID посылки - 86137293


def get_data(arr):
    data = sum(arr, [])
    result = {}
    for i in range(1, 10):
        result[str(i)] = 0
        for value in data:
            if value == i:
                result[str(i)] += 1
    return result


def count_hits(k_value, arr):
    data = get_data(arr)
    count = 0
    for _, value in data.items():
        if 0 < value <= k_value * 2:
            count += 1
    return count


def replace_dot(string):
    return [int(i) if i != '.' else int(i.replace('.', '0')) for i in string]


def read_input():
    k_value = int(input())

    arr = []
    for i in range(4):
        arr.append(replace_dot(input().strip()))

    return k_value, arr


k, matrix = read_input()
print(count_hits(k, matrix))
