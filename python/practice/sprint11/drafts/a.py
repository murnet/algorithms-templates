def find_shortest_path_to_wastelands(street_length, street):
    left = [float('inf')] * street_length
    right = [float('inf')] * street_length

    for i in range(street_length):
        if street[i] == 0:
            left[i] = 0
        elif i > 0:
            left[i] = left[i - 1] + 1

    for i in range(street_length - 1, -1, -1):
        if street[i] == 0:
            right[i] = 0
        elif i < street_length - 1:
            right[i] = right[i + 1] + 1

    nearest_wasteland = [
        min(left[i], right[i]) for i in range(street_length)
    ]

    return ' '.join(list(map(str, nearest_wasteland)))


def read_input():
    n = int(input())
    arr = list(map(int, input().split()))
    return n, arr


n, arr = read_input()
print(find_shortest_path_to_wastelands(n, arr))
