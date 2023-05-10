OPENING_BRACKETS = ['(', '[', '{']
CLOSING_BRACKETS = [')', ']', '}']


def is_correct_bracket_seq(sequence):
    stack = []
    for br in sequence:
        if br in OPENING_BRACKETS:
            stack.append(br)
        elif br in CLOSING_BRACKETS:
            position = CLOSING_BRACKETS.index(br)
            if (len(stack) > 0) and (
                OPENING_BRACKETS[position] == stack[len(stack) - 1]
            ):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    return False


def read_input():
    brackets = input().strip()
    return brackets


def main():
    bracket_seq = read_input()
    print(is_correct_bracket_seq(bracket_seq))


if __name__ == '__main__':
    main()
data = ['{[]{()}}', '()', '', '[{}{})(]', '((()']
for seq in data:
    print(is_correct_bracket_seq(seq))
