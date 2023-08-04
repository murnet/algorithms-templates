def counting_sort_old(array, k):
    counted_values = [0] * (k + 1)
    for value in array:
        counted_values[value] += 1

    index = 0
    for value in range(k):
        for _ in range(counted_values[value]):
            array[index] = value
            index += 1

    return array


def wardrobe(array):
    pink, yellow, crimson = [], [], []
    for color in array:
        if color == '0':
            pink.append(color)
        elif color == '1':
            yellow.append(color)
        else:
            crimson.append(color)

    return pink + yellow + crimson


if __name__ == '__main__':
    _ = input()
    arr = [num for num in input().split()]
    # test = [i for i in '0 2 1 2 0 0 1'.split()]
    print(*wardrobe(arr))
