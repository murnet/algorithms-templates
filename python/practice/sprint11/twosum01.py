def twosum(numbers, X):
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == X:
                return numbers[i], numbers[j]
    # По условию задачи пара обязательно должна найтись.
    # Но предусмотрительность не помешает:
    # если пара не найдена - вернём None, None (или можно выкинуть exception).
    return None


if __name__ == '__main__':
    arr = [60, 92, -61, -29, 54, -21, -8, -39, -84, 62]
    x = -122
    # print(twosum([2, 1, 3, 5, 5], 4))
    print(twosum(arr, x))
