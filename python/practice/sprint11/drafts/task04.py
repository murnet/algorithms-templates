from typing import List


def get_weather_randomness_old(temps: List[int]) -> int:
    n = len(temps)
    if n == 1:
        return 1
    count = 0
    last_idx = n - 1
    for i, value in enumerate(temps):
        if i == 0:
            continue
        if i != last_idx:
            if temps[i - 1] < value > temps[i + 1]:
                count += 1
        else:
            if temps[i - 1] < value:
                count += 1
    return count

def get_weather_randomness_oldone(temperatures: List[int]) -> int:
    temp = [min(temperatures) - 1] + temperatures + [min(temperatures) - 1]
    count = len([n for n in range(1, len(temp)) if
                temp[n - 1] < temp[n] > temp[n + 1]])
    return count


def get_weather_randomness(temperatures: List[int]) -> int:
    if len(temperatures) <= 1:
        return 1

    count = 0
    for i in range(1, len(temperatures) - 1):
        if temperatures[i] > temperatures[i - 1] and temperatures[i] > \
                temperatures[i + 1]:
            count += 1

    if temperatures[0] > temperatures[1]:
        count += 1

    if temperatures[-1] > temperatures[-2]:
        count += 1

    return count


if __name__ == "__main__":
    ex01 = [-1, -10, -8, 0, 2, 0, 5]  # 3
    ex02 = [1, 2, 5, 4, 8]  # 2
    ex03 = list(map(int, "-159 -248 8 -23 -45 -131 -169 -184 159 -241".split()))  # 3
    print(get_weather_randomness(ex01))
    print(get_weather_randomness(ex02))
    print(get_weather_randomness(ex03))

