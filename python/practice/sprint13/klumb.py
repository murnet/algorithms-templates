def find_kub(array, kubs):
    j = 0
    res_arr = []
    array.sort()
    while j < kubs - 1:
        if array[j][1] >= array[j + 1][0]:
            if array[j][1] <= array[j + 1][1]:
                array[j][1] = array[j + 1][1]
            array[j + 1] = array[j]
        if array[j] not in res_arr:
            res_arr.append(array[j])
        j += 1
    if array[-1] not in res_arr:
        res_arr.append(array[-1])
    for i in res_arr:
        print(" ".join(list(map(str, i))))


if __name__ == '__main__':
    len_kub = int(input())
    arr = []
    for _ in range(len_kub):
        arr.append(list(map(int, input().rsplit())))
    find_kub(arr, len_kub)
