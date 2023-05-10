def change_matrix(array, rows, cols):
    result = []
    for idx in range(cols):
        column = [array[i][idx] for i in range(rows)]
        result.append(column)
    output(result)


def output(data):
    for line in data:
        print(' '.join(line))


def read_input():
    rows = int(input())
    columns = int(input())
    arr = [input().strip().split() for _ in range(rows)]
    return rows, columns, arr


def main():
    row, col, matrix = read_input()
    change_matrix(matrix, row, col)


if __name__ == '__main__':
    main()
