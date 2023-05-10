def count_dnk_strength(sequence, start, stop):
    cumulative_sums = [0]
    cg_count = 0
    for position in range(len(sequence)):
        if sequence[position] == 'C' or sequence[position] == 'G':
            cg_count += 1
        cumulative_sums.append(cg_count)
    print(cumulative_sums[start + 1] - cumulative_sums[stop])


if __name__ == '__main__':
    dnk = ['C', 'C', 'A', 'T', 'G', 'A', 'T', 'C']
    right = 7
    left = 0
    count_dnk_strength(dnk, right, left)
