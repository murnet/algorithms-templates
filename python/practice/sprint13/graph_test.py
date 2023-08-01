from rcviz import callgraph, viz


@viz
def foo(search, left, right, pairs):
    if left == pairs and right == pairs:
        print(
            left,
            right,
            'done',
        )
        print(search)
    else:
        print(
            left,
            right,
            'else',
        )
        if left < pairs:
            print(left, right, 'left')
            foo(search + '(', left + 1, right, pairs)
        if right < left:
            print(left, right, 'right')
            foo(search + ')', left, right + 1, pairs)


foo('', 0, 0, 3)
callgraph.render("foo.png")
