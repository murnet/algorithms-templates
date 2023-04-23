# ID посылки - 86244371
SQUARE_SIDE_SIZE = 4


def collect_data(arr):
    data = sum(arr, [])
    result = {}
    for i in range(1, 10):
        result[str(i)] = 0
        for value in data:
            if value == i:
                result[str(i)] += 1
    return result


def count_hits(k_value, arr):
    data = collect_data(arr)
    count = 0
    for value in data.values():
        if 0 < value <= k_value * 2:
            count += 1
    return count


def replace_dots(string):
    return [int(i) if i != '.' else int(i.replace('.', '0')) for i in string]


def read_input():
    k_value = int(input())

    arr = []
    for i in range(SQUARE_SIDE_SIZE):
        arr.append(replace_dots(input().strip()))

    return k_value, arr


if __name__ == '__main__':
    k, matrix = read_input()
    print(count_hits(k, matrix))
