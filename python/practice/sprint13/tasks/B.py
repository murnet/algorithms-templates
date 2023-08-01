data = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
}


def combination(number):
    alphabet = [data[int(i)] for i in number]
    print(alphabet)


if __name__ == '__main__':
    combination('23')
