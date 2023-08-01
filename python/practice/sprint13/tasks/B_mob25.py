from rcviz import callgraph, viz


def combination(digits):
    res = []
    backtrack(digits, '', res)
    for x in res:
        print(x, end=' ')


@viz
def backtrack(digits, string, result):
    letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    if digits == '':
        result.append(string)
        return
    for letter in letters[digits[0]]:
        string += letter
        backtrack(digits[1:], string, result)
        string = string[:-1]


if __name__ == '__main__':
    number = input()
    combination(number)
    callgraph.render('b.svg')
