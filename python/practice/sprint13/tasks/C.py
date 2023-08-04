def subsequence(substring, whole_line):
    position = -1
    for i in substring:
        position = whole_line.find(i, position + 1)
        print(position, i)
        if position == -1:
            return False
    return True


if __name__ == '__main__':
    substring = 'axc'
    whole_line = 'ahbgdcu'
    print(subsequence(substring, whole_line))
