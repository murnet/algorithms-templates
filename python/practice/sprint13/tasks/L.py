def binary_search(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] >= x and (arr[mid - 1] < x or mid == 0):
        return mid + 1
    elif x <= arr[mid]:
        return binary_search(arr, x, left, mid)
    else:
        return binary_search(arr, x, mid + 1, right)


if __name__ == '__main__':
    number_of_days = int(input())
    money_per_day = [int(num) for num in (input().split())]
    bicycle_cost = int(input())
    print(
        binary_search(money_per_day, bicycle_cost, 0, len(money_per_day)),
        end=' ',
    )
    print(
        binary_search(money_per_day, bicycle_cost * 2, 0,
                      len(money_per_day)), end=' ',
    )
