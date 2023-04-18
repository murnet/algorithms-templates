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
    # nums = [i for i in range(0, 256, 3)]
    arr = [60, 92, -61, -29, 54, -21, -8, -39, -84, 62]
    x = 46
    print(twosum_extra_ds(arr, x))
