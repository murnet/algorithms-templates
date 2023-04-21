def check_parity(arr: list) -> bool:
    # Здесь реализация вашего решения
    even = [i for i in arr if abs(i) % 2 == 0]
    odd = [i for i in arr if abs(i) % 2 != 0]
    if len(even) == 3:
        print('WIN')
        return True
    if len(odd) == 3:
        print('WIN')
        return True
    print('FAIL')
    return False


if __name__ == '__main__':
    data_list = [[7, 11, 7], [1, 2, -3], [6, -2, 0]]
    for data in data_list:
        check_parity(data)
