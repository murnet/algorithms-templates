def binary_search(arr, x, left, right):
    if right < left:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == x:
        return mid + 1
    elif arr[mid] < x:
        return binary_search(arr, x, mid + 1, right)
    else:
        return binary_search(arr, x, left, mid - 1)


if __name__ == '__main__':
    result = []
    number_of_days = 6
    money_per_day = [1, 2, 4, 4, 4, 4]
    bicycle_cost = 1

    day_to_buy_bicycle = binary_search(
        money_per_day, bicycle_cost, 0, len(money_per_day) - 1
    )
    day_to_buy_two_bicycles = binary_search(
        money_per_day, bicycle_cost * 2, 0, len(money_per_day) - 1
    )

    print(day_to_buy_bicycle, day_to_buy_two_bicycles)
