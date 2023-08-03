def concat_compare(num_1, num_2):
    return str(num_2) + str(num_1) > str(num_1) + str(num_2)

def largest_number_formed(array, compare_func):
    for i in range(1, len(array)):
        current_item = array[i]
        j = i - 1
        while j >= 0 and compare_func(array[j], current_item):  # Modified the condition
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current_item
    return array