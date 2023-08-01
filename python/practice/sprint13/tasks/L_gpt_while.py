def binary_search(arr, x):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == x:
            return mid + 1

        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':
    result = []
    number_of_days = 6
    money_per_day = [1, 2, 4, 4, 4, 4]
    bicycle_cost = 1

    day_to_buy_bicycle = binary_search(money_per_day, bicycle_cost)
    day_to_buy_two_bicycles = binary_search(money_per_day, bicycle_cost * 2)

    print(day_to_buy_bicycle, day_to_buy_two_bicycles)
