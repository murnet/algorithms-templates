def search_in_rotated_array(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        if arr[left] <= arr[mid]:  # If left half is sorted
            if arr[left] <= target < arr[mid]:  # Target is in left half
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if arr[mid] < target <= arr[right]:  # Target is in right half
                left = mid + 1
            else:
                right = mid - 1

    return -1  # Element not found


# Пример использования:
n = int(input())
k = int(input())
arr = list(map(int, input().split()))

result = search_in_rotated_array(arr, k)
print(result)
