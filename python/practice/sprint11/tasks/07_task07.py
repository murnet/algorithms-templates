def to_binary(number: int) -> str:
    # Здесь реализация вашего решения
    result = ""
    if number == 0:
        return "0"
    while number:
        result += str(number & 1)
        number = number >> 1

    result = result[::-1]

    return result


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
