# ID посылки - 89462953
from typing import List, Union


def partition(array: List[Union[int, str]], low: int, high: int) -> int:
    pivot = array[high]
    i = low
    for j in range(low, high):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]
    return i


def quicksort(array: List[Union[int, str]], low: int, high: int) -> None:
    if low > high:
        return None
    pi = partition(array, low, high)
    quicksort(array, low, pi - 1)
    quicksort(array, pi + 1, high)


def comparator(player: List[str]) -> List[Union[int, str]]:
    tasks_score, fines, username = -int(player[1]), int(player[2]), player[0]
    return [tasks_score, fines, username]


if __name__ == '__main__':
    num = int(input())
    array = [comparator(input().split()) for _ in range(num)]
    quicksort(array, low=0, high=len(array) - 1)
    for player in array:
        print(player[-1])
