def moving_average(timeseries, K):
    result = []  # Пустой массив.
    # Первый раз вычисляем значение честно и сохраняем результат.
    current_sum = sum(timeseries[0:K])
    result.append(current_sum / K)
    for i in range(0, len(timeseries) - K):
        current_sum -= timeseries[i]
        current_sum += timeseries[i + K]
        current_avg = round(current_sum / K, 2)
        result.append(current_avg)
    return result


if __name__ == "__main__":
    print(moving_average([4, 3, 8, 1, 5, 6, 3], 3))
