binary_values = [2**i for i in range(8)][::-1]


def dec_to_bin(number: int) -> str:
    result = ""
    if number == 0:
        return "0"
    while number:
        result += str(number & 1)
        number = number >> 1

    result = result[::-1]

    return result
