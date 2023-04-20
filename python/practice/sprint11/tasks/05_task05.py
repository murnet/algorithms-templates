def get_longest_word(line: str) -> str:
    # Здесь реализация вашего решения
    words = line.strip().split()
    max_len = 0
    result = []
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
            result.append(word)
    return result.pop()


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
