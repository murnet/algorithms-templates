'''
Представьте себе онлайн-игру для поездки в метро: игрок нажимает на кнопку, и
на экране появляются три случайных числа. Если все три числа оказываются одной чётности, игрок выигрывает.
Напишите программу, которая по трём числам определяет, выиграл игрок или нет.

Формат ввода
В первой строке записаны три случайных целых числа a, b и c.
Числа не превосходят 10**9 по модулю.

Формат вывода
Выведите «WIN», если игрок выиграл, и «FAIL» в противном случае.

Пример 1
Ввод
1 2 -3
Вывод
FAIL
Пример 2
Ввод
7 11 7
Вывод
WIN
Пример 3
Ввод
6 -2 0
Вывод
WIN
'''


def check_parity(a: int, b: int, c: int) -> bool:
    data = [a,b,c]
    even = [i for i in data if abs(i) % 2 == 0]
    odd = [i for i in data if abs(i) % 2 != 0]
    if len(even) == 3:
        return True
    if len(odd) == 3:
        return True
    return False


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
