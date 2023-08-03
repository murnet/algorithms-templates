def bubble_sort(n, array):
    for i in range(n - 1):
        already_sorted = True
        count = 0
        for j in range(n - i - 1):
            count += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted and count == 0:
            print(' '.join(map(str, array)))
            break
        print(' '.join(map(str, array)))


if __name__ == '__main__':
    n = 5
    arr = [4, 6, 1, 9, 3]
    bubble_sort(n, arr)
