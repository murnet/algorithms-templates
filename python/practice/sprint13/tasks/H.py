def compare_nums(num_1, num_2):
    return str(num_1) + str(num_2) > str(num_2) + str(num_1)


def big_number(array, compare_func):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i - 1
        while j >= 0 and compare_func(item_to_insert, array[j]):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = item_to_insert
    return ''.join(map(str, array))


if __name__ == '__main__':
    _ = input()
    arr = [int(num) for num in (input().split())]

    print(big_number(arr, compare_nums))
