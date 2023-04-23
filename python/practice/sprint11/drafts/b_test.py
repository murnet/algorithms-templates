def get_data(matrix):
    data = sum(matrix, [])
    result = {}
    for i in range(1, 10):
        result[str(i)] = 0
        for value in data:
            if value == i:
                result[str(i)] += 1
    return result


def check_hits(k, matrix):
    data = get_data(matrix)
    count = 0
    for _, value in data.items():
        if 0 < value <= k * 2:
            count += 1
    return count


k_value = 3
arr = [
    [1, 2, 3, 1],
    [2, 0, 0, 2],
    [2, 0, 0, 2],
    [2, 0, 0, 2]
]

print(check_hits(k_value, arr))
