def change_matrix(array, rows, cols):
    res = []
    total = []
    idx = 0
    while idx <= cols - 1:
        for i in range(rows):
            res.append(array[i][idx])
        total.append(res)
        idx += 1
        res = []
    return output(total)


def output(data):
    for line in data:
        print(' '.join(line))


def read_input():
    rows = int(input())
    column = int(input())

    arr = []
    for i in range(rows):
        arr.append(input().strip().split())

    return rows, column, arr


if __name__ == '__main__':
    row, col, matrix = read_input()
    change_matrix(matrix, row, col)
