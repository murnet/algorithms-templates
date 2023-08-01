def nesting_doll(size, n):
    if n >= 1:
        print(f'build the bottom of the nesting doll of size {size}')
        nesting_doll(size-1, n-1)
        print(f'build the top of the nesting doll of size {size}')
    else:
        return


def stairs_builder(n):
    if n == 0:
        return
    stairs_builder(n - 1)
    print(f'stairs step {n}')


def as_binary_string(n):
    if n < 0:
        return "-" + as_binary_string(-n)
    if n == 0 or n == 1:
        return str(n)
    last_digit = n % 2
    return as_binary_string(n // 2) + str(last_digit)


# nesting_doll(4, 3)
# stairs_builder(20)
print(as_binary_string(21))
