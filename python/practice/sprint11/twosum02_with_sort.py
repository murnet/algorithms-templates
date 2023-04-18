def twosum_with_sort(numbers, X):
    numbers.sort()

    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == X:
            return numbers[left], numbers[right]
        if current_sum < X:
            left += 1
        else:
            right -= 1
    return None, None


if __name__ == '__main__':
    arr = [60, 92, -61, -29, 54, -21, -8, -39, -84, 62]
    x = 46
    print(twosum_with_sort(arr, x))
