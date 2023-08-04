def search_in_rotated_array(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:  # Left half is sorted
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# Example usage:
n = int(input())
k = int(input())
arr = list(map(int, input().split()))

result = search_in_rotated_array(arr, k)
print(result)
