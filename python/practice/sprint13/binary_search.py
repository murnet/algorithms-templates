def binary_search(arr, x, left, right):
    if right <= left:  # base case # 1
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid  # base case # 2
    elif x < arr[mid]:
        return binary_search(arr, x, left, mid)  # arr[mid] < x
    else:
        return binary_search(arr, x, mid + 1, right)


if __name__ == '__main__':
    array = [i for i in range(1, 111, 4)]
    days = [1, 2, 4, 4, 6, 8]
    print(binary_search(array, 93, 0, len(array)))
    print(binary_search(days, 3, 0, len(days)))
