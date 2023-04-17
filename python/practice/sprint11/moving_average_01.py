def moving_average(timeseries, K):
    result = []
    for begin_index in range(0, len(timeseries) - K + 1):
        end_index = begin_index + K
        # Просматриваем окно шириной K.
        current_sum = 0
        for v in timeseries[begin_index:end_index]:
            current_sum += v
        current_avg = round(current_sum / K, 2)
        result.append(current_avg)
    return result


if __name__ == "__main__":
    print(moving_average([4, 3, 8, 1, 5, 6, 3], 3))
