number_of_bottles = 99

multiline_f_string = (
    f'{number_of_bottles} bottles of beer on the wall. '
    f'{number_of_bottles} bottles of beer. '
    'Take one down, pass it around, '
    f'{number_of_bottles - 1} bottles of beer on the wall.'
)

single_line_f_string = f'{number_of_bottles} bottles of beer on the wall. {number_of_bottles} bottles of beer. Take one down, pass it around, {number_of_bottles - 1} bottles of beer on the wall.'

print(multiline_f_string == single_line_f_string)
print(multiline_f_string)
print(single_line_f_string)