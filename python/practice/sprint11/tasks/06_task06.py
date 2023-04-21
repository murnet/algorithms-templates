import string


def is_palindrome(line: str) -> bool:
    # Здесь реализация вашего решения
    formatted_line = ''.join(
        [
            i.lower()
            for i in line
            if i not in string.punctuation and i not in string.whitespace
        ]
    )
    if formatted_line == formatted_line[::-1]:
        return True
    return False


print(is_palindrome(input().strip()))
