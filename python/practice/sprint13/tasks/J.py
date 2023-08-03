def bubble_sort(n, array):
    already_sorted = True
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = True
        if already_sorted:
            print(' '.join(map(str, array)))
            already_sorted = False


if __name__ == '__main__':
    length = int(input())
    arr = [int(num) for num in (input().split())]
    bubble_sort(length, arr)
