def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high -1)

        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)


def comparator(player):  # 'gena 6 1000'
    return [-int(player[1]), int(player[2]), player[0]]


if __name__ == '__main__':
    num = int(input())
    array = [comparator(input().split()) for _ in range(num)]
    quicksort(array, low=0, high=len(array))
    print(*(list(zip(*array))[-1]), sep='\n')

