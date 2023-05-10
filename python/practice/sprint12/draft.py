def change(array, row, col):
    res = []
    total = []
    idx = 0
    while idx <= col - 1:
        for i in range(row):
            print(f'{i=},{idx=} => {array[i][idx]=}')
            res.append(array[i][idx])
        total.append(res)
        idx += 1
        res = []
    return total


if __name__ == '__main__':
    data = [[1, 2, 3], [0, 2, 6], [7, 4, 1], [2, 7, 0]]
    print(change(data, 4, 3))
