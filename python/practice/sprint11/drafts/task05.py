def get_longest_word(line):
    # Здесь реализация вашего решения
    words = line.strip().split()
    max_len = 0
    result = []
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
            result.append(word)
    return result.pop()


print(get_longest_word('i love segment tree'))


# from chat gpt -
def find_longest_string(lst):
    longest_str = ""
    for string in lst:
        if len(string) > len(longest_str):
            longest_str = string
    return longest_str
