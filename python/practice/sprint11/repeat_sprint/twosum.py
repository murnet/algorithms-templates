
def twosum(nums, x):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == x:
                return nums[i], nums[j]
    return None, None


def twosum_with_sort(numbers, X):
    # Сортируем исходный массив стандартной функцией.
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
    # Если ничего не нашлось в цикле, значит, нужной пары элементов в массиве нет.
    return None, None


def twosum_extra_ds(numbers, X):
    # Создаём вспомогательную структуру данных с быстрым поиском элемента.
    previous = set()

    for A in numbers:
        Y = X - A
        if Y in previous:
            return A, Y
        else:
            previous.add(A)

    # Если ничего не нашлось в цикле, значит, нужной пары элементов в массиве нет.
    return None, None


if __name__ == '__main__':
    num_a = [2, 1, 3, 5, 5]
    num_b = [2, 1, 5, 5, 3]
    print(twosum(num_a, 4))
    print(twosum(num_b, 4))
    print(twosum_with_sort(num_a, 4))
    print(twosum_with_sort(num_b, 4))
    print(twosum_extra_ds(num_a, 4))
    print(twosum_extra_ds(num_b, 4))
