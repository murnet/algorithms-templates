from typing import List

matrix = [[1, 2, 3], [0, 2, 6], [7, 4, 1], [2, 7, 0]]
n = 4
m = 3
row = 1
col = 1

# print(matrix[3])
# print(matrix[3][0])

x = matrix[row][col]
a = matrix[row - 1][col]
b = matrix[row][col + 1]

m = 3


def get_neighbours_old(
    matrix: List[List[int]], row: int, col: int
) -> List[int]:
    # Здесь реализация вашего решения
    if row == len(matrix) - 1 and len(matrix) > 2:
        if col == len(matrix[row]) - 1:
            left = matrix[row][col - 1]
            upper = matrix[row - 1][col]
            return upper, left
        if col == 0:
            right = matrix[row][col + 1]
            upper = matrix[row - 1][col]
            return right, upper
    if row == 0:
        if col == len(matrix[row]) - 1:
            left = matrix[row][col - 1]
            down = matrix[row + 1][col]
            return left, down
        if col == 0:
            right = matrix[row][col + 1]
            down = matrix[row + 1][col]
            return down, right
    else:
        right = matrix[row][col + 1]
        upper = matrix[row - 1][col]
        left = matrix[row][col - 1]
        down = matrix[row + 1][col]
        return right, upper, left, down


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> str:
    neighbours = []
    if col > 0:
        neighbours.append(matrix[row][col - 1])
    if row > 0:
        neighbours.append(matrix[row - 1][col])
    if col < len(matrix[row]) - 1:
        neighbours.append(matrix[row][col + 1])
    if row < len(matrix) - 1:
        neighbours.append(matrix[row + 1][col])
    return ' '.join(map(str, sorted(neighbours)))


print(get_neighbours(matrix, row, col))
