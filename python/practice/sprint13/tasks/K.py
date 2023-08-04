def merge(arr, lf, mid, rg):
    left_array = arr[lf:mid]
    right_array = arr[mid:rg]

    i = j = 0
    k = lf

    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1

    while i < len(left_array):
        arr[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        arr[k] = right_array[j]
        j += 1
        k += 1

    return arr


def merge_sort(arr, lf, rg):
    if rg - lf <= 1:
        return

    mid = (lf + rg) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)
    merge(arr, lf, mid, rg)

