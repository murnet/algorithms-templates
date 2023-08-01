from rcviz import callgraph, viz


@viz
def bracket_sequence(count, string='', left=0, right=0):
    if left == count and right == count:
        print(string)
    else:
        if left < count:
            bracket_sequence(count, string + '(', left + 1, right)
        if right < left:
            bracket_sequence(count, string + ')', left, right + 1)


if __name__ == '__main__':
    number_of_brackets = int(input())
    bracket_sequence(number_of_brackets)
    callgraph.render('a.svg')
