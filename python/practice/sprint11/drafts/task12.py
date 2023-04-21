def get_extra_letter(shorter, longer):
    freq_longer = {}
    for c in longer:
        freq_longer[c] = freq_longer.get(c, 0) + 1

    for c in shorter:
        freq_longer[c] -= 1

    for c in freq_longer:
        if freq_longer[c] == 1:
            print(c)
            break


shorter = 'abcd'
longer = 'abcde'
get_extra_letter(shorter, longer)
