def two_sum(nums, X):
    for i in range(len(nums)):  # IndexError: list index out of range
        if nums[i] + nums[i + 1] == X:
            return nums[i], nums[i + 1]
    return None


def two_sum_01(nums, X):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == X:
                return nums[i], nums[j]
    return None


def two_sum_sort(nums, X):
    nums.sort()
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == X:
            return nums[left], nums[right]
        if current_sum > X:
            right -= 1
        else:
            left += 1
    return None


def two_sum_extra_ds(nums, X):
    previous = set()

    for A in nums:
        Y = X - A
        if Y in previous:
            return A, Y
        else:
            previous.add(A)
    return None


if __name__ == '__main__':
    data = [2, 1, 5, 5, 3]
    x = 4
    print(two_sum_extra_ds(data, x))
