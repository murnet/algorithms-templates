from rcviz import callgraph, viz


@viz
def gen_binary(n, prefix):
    if n == 0:
        print(prefix)
    else:
        gen_binary(n - 1, prefix + '0')
        gen_binary(n - 1, prefix + '1')
        gen_binary(n - 1, prefix + '2')


if __name__ == '__main__':
    gen_binary(3, '')
    callgraph.render('gen_binary.svg')
