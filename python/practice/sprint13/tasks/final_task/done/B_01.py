# ID посылки - 89459901
def partition(array, low, high):
    pivot = array[high]
    i = low
    for j in range(low, high):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]
    return i


def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)


def comparator(player):
    return [-int(player[1]), int(player[2]), player[0]]


if __name__ == '__main__':
    num = int(input())
    array = [comparator(input().split()) for _ in range(num)]
    quicksort(array, low=0, high=len(array) - 1)
    print(*(list(zip(*array))[-1]), sep='\n')
